"""
Token Counter and Tokenization Demo
=====================================
Module 01 - Foundations of Artificial Intelligence
Code Example 1: Understanding Tokens

This script demonstrates how to count tokens using tiktoken (for OpenAI models)
and shows how text is broken into tokens. It also compares tokenization across
different encodings and languages.

Requirements:
    pip install tiktoken

Usage:
    python token-counter.py
"""

import sys

try:
    import tiktoken
except ImportError:
    print("Error: tiktoken is not installed.")
    print("Install it with: pip install tiktoken")
    print()
    sys.exit(1)


# =============================================================================
# SECTION 1: Basic Token Counting
# =============================================================================

def count_tokens(text: str, model: str = "gpt-4o") -> dict:
    """
    Count the number of tokens in a text string for a given model.

    Args:
        text: The text to tokenize.
        model: The model name to use for encoding (default: gpt-4o).

    Returns:
        A dictionary with token count, tokens, and decoded tokens.
    """
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    decoded_tokens = [encoding.decode([token]) for token in tokens]

    return {
        "text": text,
        "model": model,
        "encoding_name": encoding.name,
        "token_count": len(tokens),
        "token_ids": tokens,
        "decoded_tokens": decoded_tokens,
    }


def print_token_info(result: dict) -> None:
    """Pretty-print token counting results."""
    print(f"  Text:           \"{result['text']}\"")
    print(f"  Model:          {result['model']}")
    print(f"  Encoding:       {result['encoding_name']}")
    print(f"  Token count:    {result['token_count']}")
    print(f"  Token IDs:      {result['token_ids']}")
    print(f"  Decoded tokens: {result['decoded_tokens']}")
    print()


# =============================================================================
# SECTION 2: Comparing Different Texts
# =============================================================================

def demo_basic_tokenization():
    """Demonstrate basic tokenization with various text examples."""
    print("=" * 70)
    print("DEMO 1: Basic Tokenization")
    print("=" * 70)
    print()

    examples = [
        "Hello",
        "Hello, world!",
        "Artificial Intelligence",
        "tokenization",
        "The quick brown fox jumps over the lazy dog.",
        "GPT-4 is a large language model.",
        "supercalifragilisticexpialidocious",
        "12345",
        "def hello(): print('hi')",
        "https://www.example.com/path?query=value",
    ]

    for text in examples:
        result = count_tokens(text)
        print_token_info(result)


# =============================================================================
# SECTION 3: Comparing Encodings
# =============================================================================

def demo_encoding_comparison():
    """Compare tokenization across different OpenAI encodings."""
    print("=" * 70)
    print("DEMO 2: Comparing Encodings (GPT-3.5 vs GPT-4 vs GPT-4o)")
    print("=" * 70)
    print()

    text = "Artificial Intelligence is transforming the world in remarkable ways."

    # Different encodings used by different model generations
    encodings_to_compare = [
        ("cl100k_base", "GPT-4 / GPT-3.5 Turbo"),
        ("o200k_base", "GPT-4o"),
    ]

    print(f"  Text: \"{text}\"")
    print()

    for enc_name, model_desc in encodings_to_compare:
        try:
            encoding = tiktoken.get_encoding(enc_name)
            tokens = encoding.encode(text)
            decoded = [encoding.decode([t]) for t in tokens]
            print(f"  Encoding: {enc_name} ({model_desc})")
            print(f"  Token count: {len(tokens)}")
            print(f"  Tokens: {decoded}")
            print()
        except Exception as e:
            print(f"  Encoding {enc_name}: Not available ({e})")
            print()


# =============================================================================
# SECTION 4: Language Comparison
# =============================================================================

def demo_language_comparison():
    """Show how different languages require different numbers of tokens."""
    print("=" * 70)
    print("DEMO 3: Language Comparison (Same Meaning, Different Token Counts)")
    print("=" * 70)
    print()

    # "Hello, how are you?" in different languages
    translations = {
        "English":    "Hello, how are you?",
        "Spanish":    "Hola, como estas?",
        "French":     "Bonjour, comment allez-vous?",
        "German":     "Hallo, wie geht es Ihnen?",
        "Italian":    "Ciao, come stai?",
        "Portuguese": "Ola, como voce esta?",
        "Japanese":   "こんにちは、お元気ですか？",
        "Chinese":    "你好，你怎么样？",
        "Korean":     "안녕하세요, 어떻게 지내세요?",
        "Arabic":     "مرحبا، كيف حالك؟",
        "Russian":    "Привет, как дела?",
        "Hindi":      "नमस्ते, आप कैसे हैं?",
    }

    encoding = tiktoken.encoding_for_model("gpt-4o")

    print(f"  {'Language':<15} {'Text':<35} {'Tokens':>7}  {'Ratio vs English':>16}")
    print(f"  {'-' * 15} {'-' * 35} {'-' * 7}  {'-' * 16}")

    english_count = len(encoding.encode(translations["English"]))

    for lang, text in translations.items():
        tokens = encoding.encode(text)
        count = len(tokens)
        ratio = count / english_count
        print(f"  {lang:<15} {text:<35} {count:>7}  {ratio:>15.2f}x")

    print()
    print("  Key insight: Non-Latin scripts typically use 1.5-3x more tokens")
    print("  for the same meaning, making them more expensive to process.")
    print()


# =============================================================================
# SECTION 5: Code Tokenization
# =============================================================================

def demo_code_tokenization():
    """Show how programming code is tokenized."""
    print("=" * 70)
    print("DEMO 4: Code Tokenization")
    print("=" * 70)
    print()

    code_examples = {
        "Python function": '''def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)''',

        "JavaScript arrow": '''const greet = (name) => {
    return `Hello, ${name}!`;
};''',

        "SQL query": '''SELECT users.name, COUNT(orders.id)
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.name
HAVING COUNT(orders.id) > 5;''',

        "JSON data": '''{
    "name": "John Doe",
    "age": 30,
    "email": "john@example.com"
}''',
    }

    encoding = tiktoken.encoding_for_model("gpt-4o")

    for name, code in code_examples.items():
        tokens = encoding.encode(code)
        lines = code.count("\n") + 1
        chars = len(code)
        print(f"  {name}:")
        print(f"  {'.' * 50}")
        for line in code.split("\n"):
            print(f"    {line}")
        print(f"  {'.' * 50}")
        print(f"  Lines: {lines} | Characters: {chars} | Tokens: {len(tokens)}")
        print(f"  Chars per token: {chars / len(tokens):.1f}")
        print()


# =============================================================================
# SECTION 6: Cost Calculator
# =============================================================================

def demo_cost_calculator():
    """Calculate the cost of processing text with different models."""
    print("=" * 70)
    print("DEMO 5: Cost Calculator")
    print("=" * 70)
    print()

    # Sample text (approximately one paragraph)
    sample_text = """
    Artificial Intelligence has undergone a remarkable transformation in recent
    years, evolving from a niche academic pursuit into one of the most impactful
    technologies of the 21st century. The advent of large language models,
    particularly the Transformer architecture introduced in 2017, has enabled
    machines to understand and generate human language with unprecedented fluency.
    Companies like OpenAI, Anthropic, Google, and Meta are now competing to build
    increasingly capable AI systems that can reason, create, and assist humans
    across virtually every domain of work and creativity.
    """

    encoding = tiktoken.encoding_for_model("gpt-4o")
    input_tokens = len(encoding.encode(sample_text))

    # Assume the model generates a response roughly equal in length
    estimated_output_tokens = input_tokens

    # Pricing per 1M tokens (approximate, as of early 2026)
    pricing = {
        "GPT-4o": {"input": 2.50, "output": 10.00},
        "GPT-4o mini": {"input": 0.15, "output": 0.60},
        "Claude 3.5 Sonnet": {"input": 3.00, "output": 15.00},
        "Claude 3.5 Haiku": {"input": 0.80, "output": 4.00},
        "Claude Opus 4": {"input": 15.00, "output": 75.00},
        "Gemini 1.5 Pro": {"input": 1.25, "output": 5.00},
        "Gemini 1.5 Flash": {"input": 0.075, "output": 0.30},
    }

    print(f"  Sample text tokens: {input_tokens}")
    print(f"  Estimated output tokens: {estimated_output_tokens}")
    print()
    print(f"  {'Model':<25} {'Input Cost':>12} {'Output Cost':>13} {'Total Cost':>12} {'Per 1K calls':>13}")
    print(f"  {'-' * 25} {'-' * 12} {'-' * 13} {'-' * 12} {'-' * 13}")

    for model, prices in pricing.items():
        input_cost = (input_tokens / 1_000_000) * prices["input"]
        output_cost = (estimated_output_tokens / 1_000_000) * prices["output"]
        total = input_cost + output_cost
        per_1k = total * 1000
        print(
            f"  {model:<25} ${input_cost:>10.6f} ${output_cost:>11.6f} ${total:>10.6f} ${per_1k:>11.4f}"
        )

    print()
    print("  Note: Prices are approximate and change frequently.")
    print("  Always check the provider's current pricing page.")
    print()


# =============================================================================
# SECTION 7: Token Estimation Helper
# =============================================================================

def demo_estimation_rules():
    """Demonstrate rules of thumb for estimating token counts."""
    print("=" * 70)
    print("DEMO 6: Token Estimation Rules of Thumb")
    print("=" * 70)
    print()

    texts = [
        "A short sentence.",
        "Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed.",
        "The quick brown fox jumps over the lazy dog. " * 10,  # ~100 words
    ]

    encoding = tiktoken.encoding_for_model("gpt-4o")

    print(f"  {'Words':>8} {'Chars':>8} {'Actual':>8} {'Est(w*1.33)':>12} {'Est(c/4)':>10} {'Word Ratio':>11} {'Char Ratio':>11}")
    print(f"  {'-' * 8} {'-' * 8} {'-' * 8} {'-' * 12} {'-' * 10} {'-' * 11} {'-' * 11}")

    for text in texts:
        words = len(text.split())
        chars = len(text)
        actual = len(encoding.encode(text))
        est_words = round(words * 1.33)
        est_chars = round(chars / 4)
        word_ratio = actual / words if words > 0 else 0
        char_ratio = chars / actual if actual > 0 else 0

        print(
            f"  {words:>8} {chars:>8} {actual:>8} {est_words:>12} {est_chars:>10} "
            f"{word_ratio:>10.2f}x {char_ratio:>10.1f}c/t"
        )

    print()
    print("  Rules of thumb:")
    print("    - 1 token is approximately 4 characters (English)")
    print("    - 1 token is approximately 0.75 words (English)")
    print("    - 100 tokens is approximately 75 words")
    print("    - 1,000 tokens is approximately 750 words or 1.5 pages")
    print()


# =============================================================================
# SECTION 8: Interactive Mode
# =============================================================================

def interactive_mode():
    """Allow the user to input text and see its tokenization."""
    print("=" * 70)
    print("INTERACTIVE MODE: Enter text to see its tokenization")
    print("Type 'quit' or 'exit' to stop")
    print("=" * 70)
    print()

    encoding = tiktoken.encoding_for_model("gpt-4o")

    while True:
        try:
            text = input("  Enter text: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if text.lower() in ("quit", "exit", "q"):
            break

        if not text:
            continue

        tokens = encoding.encode(text)
        decoded = [encoding.decode([t]) for t in tokens]

        print(f"  Token count: {len(tokens)}")
        print(f"  Token IDs:   {tokens}")
        print(f"  Tokens:      {decoded}")

        # Cost estimate for a round trip (input + similar output)
        cost_gpt4o = (len(tokens) / 1_000_000) * (2.50 + 10.00)
        cost_mini = (len(tokens) / 1_000_000) * (0.15 + 0.60)
        print(f"  Est. round-trip cost (GPT-4o):      ${cost_gpt4o:.6f}")
        print(f"  Est. round-trip cost (GPT-4o mini):  ${cost_mini:.6f}")
        print()


# =============================================================================
# MAIN
# =============================================================================

def main():
    """Run all demos."""
    print()
    print("  TOKEN COUNTER AND TOKENIZATION DEMO")
    print("  Module 01 - Foundations of Artificial Intelligence")
    print("  Master in Prompt Engineering and AI")
    print()

    demo_basic_tokenization()
    demo_encoding_comparison()
    demo_language_comparison()
    demo_code_tokenization()
    demo_cost_calculator()
    demo_estimation_rules()

    # Uncomment the following line to enable interactive mode:
    # interactive_mode()

    print("=" * 70)
    print("All demos complete!")
    print()
    print("To explore interactively, uncomment the interactive_mode()")
    print("call in main() or run: python -c \"from token_counter import interactive_mode; interactive_mode()\"")
    print("=" * 70)


if __name__ == "__main__":
    main()
