"""
Fine-Tuning Data Preparation and Validation Script
====================================================

This script provides tools for creating, validating, cleaning, and
splitting fine-tuning datasets in the JSONL chat format required by
OpenAI and compatible providers.

Requirements:
    pip install tiktoken

Usage:
    python fine-tuning-data-preparation.py

Author: Master in Prompt Engineering and AI - Module 05
"""

import json
import random
import re
import os
from typing import List, Dict, Tuple, Optional
from collections import defaultdict

try:
    import tiktoken
    TIKTOKEN_AVAILABLE = True
except ImportError:
    TIKTOKEN_AVAILABLE = False
    print("Warning: tiktoken not installed. Token counting will be estimated.")


# =============================================================================
# TOKEN COUNTING
# =============================================================================

def count_tokens(text: str, model: str = "gpt-4o") -> int:
    """Count the number of tokens in a text string."""
    if TIKTOKEN_AVAILABLE:
        try:
            encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            encoding = tiktoken.get_encoding("cl100k_base")
        return len(encoding.encode(text))
    else:
        # Rough estimate: ~4 characters per token
        return len(text) // 4


def count_message_tokens(messages: List[Dict], model: str = "gpt-4o") -> int:
    """
    Count tokens for a list of chat messages.
    Includes the overhead tokens for message formatting.
    """
    total = 0
    for message in messages:
        total += 4  # Every message has overhead tokens
        total += count_tokens(message.get("content", ""), model)
        total += count_tokens(message.get("role", ""), model)
    total += 2  # Priming tokens
    return total


# =============================================================================
# DATA CREATION HELPERS
# =============================================================================

def create_example(
    system_prompt: str,
    user_message: str,
    assistant_response: str
) -> Dict:
    """
    Create a single fine-tuning example in the chat format.

    Args:
        system_prompt: The system message defining behavior
        user_message: The user's input
        assistant_response: The desired assistant output

    Returns:
        Dict in the JSONL chat format
    """
    messages = []

    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})

    messages.append({"role": "user", "content": user_message})
    messages.append({"role": "assistant", "content": assistant_response})

    return {"messages": messages}


def create_multi_turn_example(
    system_prompt: str,
    turns: List[Tuple[str, str]]
) -> Dict:
    """
    Create a multi-turn conversation example.

    Args:
        system_prompt: The system message
        turns: List of (role, content) tuples

    Returns:
        Dict in the JSONL chat format
    """
    messages = []

    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})

    for role, content in turns:
        if role not in ("user", "assistant"):
            raise ValueError(f"Invalid role in turns: {role}")
        messages.append({"role": role, "content": content})

    return {"messages": messages}


def create_sample_dataset() -> List[Dict]:
    """
    Create a sample dataset for demonstration purposes.
    This creates examples for a customer support fine-tuning task.
    """
    system_prompt = (
        "You are a helpful customer support agent for TechStore, "
        "an electronics retailer. Be friendly, professional, and "
        "solution-oriented. Always offer next steps."
    )

    examples = [
        create_example(
            system_prompt,
            "My laptop screen is flickering.",
            "I'm sorry to hear about the screen flickering on your laptop. "
            "This can be caused by several factors. Let's troubleshoot:\n\n"
            "1. **Update display drivers**: Go to Device Manager > Display "
            "Adapters > Right-click your GPU > Update Driver.\n"
            "2. **Check refresh rate**: Settings > Display > Advanced Display "
            "Settings. Try changing the refresh rate.\n"
            "3. **Test with external monitor**: Connect to an external display "
            "to determine if it's a hardware issue.\n\n"
            "If the issue persists after these steps, it may be a hardware "
            "problem. Would you like me to help you set up a repair appointment?"
        ),
        create_example(
            system_prompt,
            "How do I return a product I bought online?",
            "I'd be happy to help you with a return! Here's our online "
            "return process:\n\n"
            "1. Log into your TechStore account at techstore.com/account\n"
            "2. Go to **Order History**\n"
            "3. Find the order and click **Request Return**\n"
            "4. Select the reason for return\n"
            "5. Choose your preferred return method (mail or in-store)\n"
            "6. Print the prepaid return label if returning by mail\n\n"
            "**Important notes:**\n"
            "- Returns are accepted within 30 days of delivery\n"
            "- Items must be in original packaging\n"
            "- Refunds are processed within 5-7 business days\n\n"
            "Is there anything else I can help you with?"
        ),
        create_example(
            system_prompt,
            "I was charged twice for my order #12345",
            "I understand how concerning a double charge can be, and I "
            "apologize for the inconvenience. Let me help resolve this.\n\n"
            "For order #12345, here's what I can do:\n\n"
            "1. I'll escalate this to our billing team for immediate review\n"
            "2. If confirmed as a duplicate charge, a refund will be "
            "initiated within 24 hours\n"
            "3. The refund typically appears on your statement within "
            "3-5 business days\n\n"
            "In the meantime, could you please:\n"
            "- Check if one charge might be a temporary authorization hold "
            "(these usually disappear within 48 hours)\n"
            "- Have your bank statement ready in case we need additional "
            "verification\n\n"
            "I've noted your concern and will follow up. Is there anything "
            "else I can assist you with?"
        ),
        create_multi_turn_example(
            system_prompt,
            [
                ("user", "I want to buy a new laptop for college."),
                ("assistant",
                 "Great choice! I'd love to help you find the perfect "
                 "laptop for college. To give you the best recommendation, "
                 "could you tell me:\n\n"
                 "1. **Budget range**: What's your price range?\n"
                 "2. **Major/use case**: What will you primarily use it "
                 "for? (e.g., writing, programming, design, gaming)\n"
                 "3. **Portability**: Do you need something lightweight "
                 "for carrying between classes?\n"
                 "4. **Operating system**: Any preference for Windows, "
                 "macOS, or ChromeOS?"),
                ("user", "Budget is around $800, computer science major, "
                 "and I want something light."),
                ("assistant",
                 "Perfect! For a computer science major with an $800 budget "
                 "who needs portability, here are my top recommendations:\n\n"
                 "**1. TechStore UltraBook Pro 14\" - $749**\n"
                 "- Intel Core i5-13500H, 16GB RAM, 512GB SSD\n"
                 "- 2.9 lbs, 10-hour battery\n"
                 "- Great for coding with a comfortable keyboard\n\n"
                 "**2. TechStore DevBook 13\" - $799**\n"
                 "- AMD Ryzen 7 7730U, 16GB RAM, 512GB SSD\n"
                 "- 2.6 lbs, 12-hour battery\n"
                 "- Linux-friendly, excellent for development\n\n"
                 "Both have enough power for IDEs, virtual machines, and "
                 "compiling code. The DevBook is lighter with better "
                 "battery, while the UltraBook Pro has a larger screen.\n\n"
                 "Would you like more details on either model, or would "
                 "you like to see other options?")
            ]
        ),
        create_example(
            system_prompt,
            "My order says delivered but I never received it.",
            "I'm really sorry about this situation. A missing delivery is "
            "understandably frustrating. Let's work together to resolve this.\n\n"
            "Here are the immediate steps:\n\n"
            "1. **Check around your property**: Sometimes packages are left "
            "at side doors, garages, or with neighbors.\n"
            "2. **Check your mailroom/front desk**: If you live in an "
            "apartment, it may have been received there.\n"
            "3. **Check the delivery photo**: If available, go to your order "
            "details for the delivery confirmation photo.\n\n"
            "If you still can't locate it:\n"
            "- I can file a delivery investigation with our shipping partner\n"
            "- If not resolved within 48 hours, we'll send a replacement or "
            "issue a full refund -- your choice\n\n"
            "Could you provide your order number so I can start the "
            "investigation right away?"
        ),
    ]

    return examples


# =============================================================================
# VALIDATION
# =============================================================================

def validate_example(example: Dict, line_num: int = 0) -> Tuple[List[str], List[str]]:
    """
    Validate a single training example.

    Returns:
        Tuple of (errors, warnings) lists
    """
    errors = []
    warnings = []
    prefix = f"Line {line_num}: " if line_num else ""

    # Check top-level structure
    if "messages" not in example:
        errors.append(f"{prefix}Missing 'messages' key")
        return errors, warnings

    messages = example["messages"]

    if not isinstance(messages, list):
        errors.append(f"{prefix}'messages' must be a list")
        return errors, warnings

    if len(messages) < 2:
        errors.append(f"{prefix}Need at least 2 messages (user + assistant)")
        return errors, warnings

    # Check each message
    valid_roles = {"system", "user", "assistant"}
    has_assistant = False
    has_user = False
    prev_role = None

    for i, msg in enumerate(messages):
        if not isinstance(msg, dict):
            errors.append(f"{prefix}Message {i} is not a dict")
            continue

        # Check role
        role = msg.get("role")
        if role is None:
            errors.append(f"{prefix}Message {i} missing 'role'")
        elif role not in valid_roles:
            errors.append(f"{prefix}Message {i} has invalid role '{role}'")
        else:
            if role == "assistant":
                has_assistant = True
            if role == "user":
                has_user = True

        # Check content
        content = msg.get("content")
        if content is None:
            errors.append(f"{prefix}Message {i} missing 'content'")
        elif not isinstance(content, str):
            errors.append(f"{prefix}Message {i} content must be a string")
        elif len(content.strip()) == 0:
            warnings.append(f"{prefix}Message {i} has empty content")
        elif len(content) < 5:
            warnings.append(f"{prefix}Message {i} content is very short "
                          f"({len(content)} chars)")

        # Check role order
        if role == "system" and i != 0:
            errors.append(f"{prefix}System message must be first (found at position {i})")
        if prev_role == "user" and role == "user":
            warnings.append(f"{prefix}Two consecutive user messages at position {i}")
        if prev_role == "assistant" and role == "assistant":
            warnings.append(f"{prefix}Two consecutive assistant messages at position {i}")

        prev_role = role

    if not has_assistant:
        errors.append(f"{prefix}No assistant message found")
    if not has_user:
        errors.append(f"{prefix}No user message found")

    # Check last message should be assistant
    if messages and messages[-1].get("role") != "assistant":
        warnings.append(f"{prefix}Last message is not from assistant "
                       f"(role: {messages[-1].get('role')})")

    # Token count check
    total_tokens = count_message_tokens(messages)
    if total_tokens > 16000:
        warnings.append(f"{prefix}High token count: {total_tokens} tokens "
                       f"(may exceed context limit)")
    elif total_tokens > 8000:
        warnings.append(f"{prefix}Moderate token count: {total_tokens} tokens")

    return errors, warnings


def validate_dataset(file_path: str) -> Dict:
    """
    Validate an entire JSONL dataset file.

    Returns:
        Dict with errors, warnings, and statistics
    """
    all_errors = []
    all_warnings = []
    stats = {
        "total_examples": 0,
        "total_tokens": 0,
        "max_tokens": 0,
        "min_tokens": float("inf"),
        "avg_tokens": 0,
        "system_prompt_count": 0,
        "multi_turn_count": 0,
        "token_distribution": defaultdict(int),
    }

    with open(file_path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue

            # Parse JSON
            try:
                example = json.loads(line)
            except json.JSONDecodeError as e:
                all_errors.append(f"Line {line_num}: Invalid JSON - {e}")
                continue

            # Validate
            errors, warnings = validate_example(example, line_num)
            all_errors.extend(errors)
            all_warnings.extend(warnings)

            # Statistics
            if "messages" in example and isinstance(example["messages"], list):
                messages = example["messages"]
                stats["total_examples"] += 1

                tokens = count_message_tokens(messages)
                stats["total_tokens"] += tokens
                stats["max_tokens"] = max(stats["max_tokens"], tokens)
                stats["min_tokens"] = min(stats["min_tokens"], tokens)

                # Token range distribution
                bucket = (tokens // 500) * 500
                stats["token_distribution"][f"{bucket}-{bucket+499}"] += 1

                # Check for system prompt
                if messages[0].get("role") == "system":
                    stats["system_prompt_count"] += 1

                # Check for multi-turn
                user_count = sum(1 for m in messages if m.get("role") == "user")
                if user_count > 1:
                    stats["multi_turn_count"] += 1

    # Calculate averages
    if stats["total_examples"] > 0:
        stats["avg_tokens"] = stats["total_tokens"] / stats["total_examples"]
    if stats["min_tokens"] == float("inf"):
        stats["min_tokens"] = 0

    stats["token_distribution"] = dict(sorted(stats["token_distribution"].items()))

    return {
        "errors": all_errors,
        "warnings": all_warnings,
        "stats": stats,
        "is_valid": len(all_errors) == 0,
    }


# =============================================================================
# DATA SPLITTING
# =============================================================================

def split_dataset(
    input_file: str,
    train_file: str,
    val_file: str,
    val_ratio: float = 0.1,
    seed: int = 42
) -> Dict:
    """
    Split a JSONL dataset into training and validation sets.

    Args:
        input_file: Path to the input JSONL file
        train_file: Path for the training output file
        val_file: Path for the validation output file
        val_ratio: Fraction of data for validation (default: 10%)
        seed: Random seed for reproducibility

    Returns:
        Dict with split statistics
    """
    # Load all examples
    examples = []
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                examples.append(json.loads(line))

    # Shuffle with seed
    random.seed(seed)
    random.shuffle(examples)

    # Split
    val_count = max(1, int(len(examples) * val_ratio))
    val_examples = examples[:val_count]
    train_examples = examples[val_count:]

    # Write files
    with open(train_file, "w", encoding="utf-8") as f:
        for ex in train_examples:
            f.write(json.dumps(ex, ensure_ascii=False) + "\n")

    with open(val_file, "w", encoding="utf-8") as f:
        for ex in val_examples:
            f.write(json.dumps(ex, ensure_ascii=False) + "\n")

    return {
        "total": len(examples),
        "train": len(train_examples),
        "validation": len(val_examples),
        "train_file": train_file,
        "val_file": val_file,
    }


# =============================================================================
# DATA CLEANING
# =============================================================================

def clean_dataset(input_file: str, output_file: str) -> Dict:
    """
    Clean a dataset by removing invalid examples and normalizing content.

    Returns:
        Dict with cleaning statistics
    """
    stats = {"total": 0, "kept": 0, "removed": 0, "fixed": 0}

    cleaned = []

    with open(input_file, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue

            stats["total"] += 1

            try:
                example = json.loads(line)
            except json.JSONDecodeError:
                stats["removed"] += 1
                continue

            errors, _ = validate_example(example)
            if errors:
                stats["removed"] += 1
                continue

            # Clean content
            fixed = False
            for msg in example.get("messages", []):
                content = msg.get("content", "")
                # Normalize whitespace
                new_content = re.sub(r"\n{3,}", "\n\n", content)
                new_content = new_content.strip()
                if new_content != content:
                    msg["content"] = new_content
                    fixed = True

            if fixed:
                stats["fixed"] += 1

            cleaned.append(example)
            stats["kept"] += 1

    with open(output_file, "w", encoding="utf-8") as f:
        for example in cleaned:
            f.write(json.dumps(example, ensure_ascii=False) + "\n")

    return stats


# =============================================================================
# COST ESTIMATION
# =============================================================================

def estimate_cost(file_path: str, model: str = "gpt-4o-mini", epochs: int = 3) -> Dict:
    """
    Estimate the fine-tuning cost for an OpenAI model.

    Returns:
        Dict with cost estimates
    """
    # Pricing per 1M tokens (approximate, as of 2025)
    pricing = {
        "gpt-4o-mini": {"training": 3.00, "input": 0.30, "output": 1.20},
        "gpt-4o": {"training": 25.00, "input": 3.75, "output": 15.00},
    }

    if model not in pricing:
        return {"error": f"Unknown model: {model}"}

    # Count tokens
    total_tokens = 0
    num_examples = 0

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            example = json.loads(line)
            tokens = count_message_tokens(example.get("messages", []))
            total_tokens += tokens
            num_examples += 1

    training_tokens = total_tokens * epochs
    cost_per_m = pricing[model]["training"]
    training_cost = (training_tokens / 1_000_000) * cost_per_m

    return {
        "model": model,
        "num_examples": num_examples,
        "total_tokens": total_tokens,
        "epochs": epochs,
        "training_tokens": training_tokens,
        "estimated_cost": f"${training_cost:.2f}",
        "input_cost_per_1k_queries": f"${(1000 * 500 / 1_000_000) * pricing[model]['input']:.2f}",
        "output_cost_per_1k_queries": f"${(1000 * 300 / 1_000_000) * pricing[model]['output']:.2f}",
    }


# =============================================================================
# MAIN - DEMO
# =============================================================================

def main():
    """Demonstrate the data preparation tools."""
    print("=" * 60)
    print("  FINE-TUNING DATA PREPARATION TOOLS")
    print("=" * 60)

    # Create sample dataset
    print("\n1. Creating sample dataset...")
    examples = create_sample_dataset()
    print(f"   Created {len(examples)} sample examples")

    # Save to file
    output_file = "sample_training_data.jsonl"
    with open(output_file, "w", encoding="utf-8") as f:
        for example in examples:
            f.write(json.dumps(example, ensure_ascii=False) + "\n")
    print(f"   Saved to: {output_file}")

    # Validate
    print("\n2. Validating dataset...")
    results = validate_dataset(output_file)

    print(f"\n   === Validation Results ===")
    print(f"   Total examples:    {results['stats']['total_examples']}")
    print(f"   Total tokens:      {results['stats']['total_tokens']:,}")
    print(f"   Avg tokens/example:{results['stats']['avg_tokens']:.0f}")
    print(f"   Min tokens:        {results['stats']['min_tokens']}")
    print(f"   Max tokens:        {results['stats']['max_tokens']}")
    print(f"   System prompts:    {results['stats']['system_prompt_count']}")
    print(f"   Multi-turn:        {results['stats']['multi_turn_count']}")
    print(f"   Valid:             {'YES' if results['is_valid'] else 'NO'}")

    if results["errors"]:
        print(f"\n   Errors ({len(results['errors'])}):")
        for err in results["errors"][:5]:
            print(f"     - {err}")

    if results["warnings"]:
        print(f"\n   Warnings ({len(results['warnings'])}):")
        for warn in results["warnings"][:5]:
            print(f"     - {warn}")

    print(f"\n   Token distribution:")
    for bucket, count in results["stats"]["token_distribution"].items():
        bar = "#" * count * 3
        print(f"     {bucket:>12s}: {bar} ({count})")

    # Estimate cost
    print("\n3. Cost estimates...")
    for model in ["gpt-4o-mini", "gpt-4o"]:
        cost = estimate_cost(output_file, model=model, epochs=3)
        print(f"\n   Model: {cost['model']}")
        print(f"   Training tokens:  {cost['training_tokens']:,}")
        print(f"   Training cost:    {cost['estimated_cost']}")

    # Clean up sample file
    print(f"\n4. Sample dataset saved to: {output_file}")
    print("   You can use this as a template for your own data.")
    print("\n   Next steps:")
    print("   - Add more examples (aim for 50-500+)")
    print("   - Run: python fine-tuning-data-preparation.py to validate")
    print("   - Split into train/val with split_dataset()")
    print("   - Upload to OpenAI for fine-tuning")


if __name__ == "__main__":
    main()
