"""
First API Call -- OpenAI and Anthropic
=======================================
Module 01 - Foundations of Artificial Intelligence
Code Example 4: Making Your First API Calls

This script demonstrates how to make your first API calls to both
OpenAI (GPT) and Anthropic (Claude). It covers basic usage, streaming,
system prompts, and error handling.

Requirements:
    pip install openai anthropic

Setup:
    Set your API keys as environment variables:

    export OPENAI_API_KEY="sk-your-key-here"
    export ANTHROPIC_API_KEY="sk-ant-your-key-here"

    Or create a .env file (never commit this to git!):
    OPENAI_API_KEY=sk-your-key-here
    ANTHROPIC_API_KEY=sk-ant-your-key-here

Usage:
    python first-api-call.py
"""

import os
import sys
import time


# =============================================================================
# HELPER: Check for API keys
# =============================================================================

def get_api_key(provider: str) -> str | None:
    """
    Get API key from environment variable.

    Args:
        provider: Either 'openai' or 'anthropic'.

    Returns:
        The API key string, or None if not found.
    """
    env_var = f"{provider.upper()}_API_KEY"
    key = os.environ.get(env_var)
    if not key:
        print(f"  WARNING: {env_var} environment variable not set.")
        print(f"  Set it with: export {env_var}=\"your-key-here\"")
        print()
    return key


# =============================================================================
# SECTION 1: OpenAI API Call
# =============================================================================

def demo_openai_basic():
    """Make a basic API call to OpenAI."""
    print("=" * 70)
    print("DEMO 1: Basic OpenAI API Call (GPT-4o mini)")
    print("=" * 70)
    print()

    api_key = get_api_key("openai")
    if not api_key:
        print("  Skipping OpenAI demo (no API key).")
        print()
        print("  Here is what the code looks like:")
        print()
        print('  from openai import OpenAI')
        print()
        print('  client = OpenAI()  # Uses OPENAI_API_KEY env var')
        print()
        print('  response = client.chat.completions.create(')
        print('      model="gpt-4o-mini",')
        print('      messages=[')
        print('          {"role": "system", "content": "You are a helpful assistant."},')
        print('          {"role": "user", "content": "What is prompt engineering?"}')
        print('      ],')
        print('      temperature=0.7,')
        print('      max_tokens=300')
        print('  )')
        print()
        print('  print(response.choices[0].message.content)')
        print()
        return

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)

        print("  Sending request to GPT-4o mini...")
        start_time = time.time()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant. Be concise and clear."
                },
                {
                    "role": "user",
                    "content": "What is prompt engineering? Explain in 3 sentences."
                }
            ],
            temperature=0.7,
            max_tokens=300,
        )

        elapsed = time.time() - start_time

        # Extract and display the response
        message = response.choices[0].message.content
        usage = response.usage

        print(f"  Response received in {elapsed:.2f} seconds")
        print()
        print(f"  Model: {response.model}")
        print(f"  Response:")
        print(f"  {'-' * 60}")
        for line in message.split("\n"):
            print(f"    {line}")
        print(f"  {'-' * 60}")
        print()
        print(f"  Token Usage:")
        print(f"    Input tokens:  {usage.prompt_tokens}")
        print(f"    Output tokens: {usage.completion_tokens}")
        print(f"    Total tokens:  {usage.total_tokens}")

        # Calculate cost (GPT-4o mini pricing)
        input_cost = (usage.prompt_tokens / 1_000_000) * 0.15
        output_cost = (usage.completion_tokens / 1_000_000) * 0.60
        total_cost = input_cost + output_cost
        print(f"    Estimated cost: ${total_cost:.6f}")
        print()

    except ImportError:
        print("  Error: openai package not installed.")
        print("  Install with: pip install openai")
        print()
    except Exception as e:
        print(f"  Error: {e}")
        print()


# =============================================================================
# SECTION 2: Anthropic API Call
# =============================================================================

def demo_anthropic_basic():
    """Make a basic API call to Anthropic Claude."""
    print("=" * 70)
    print("DEMO 2: Basic Anthropic API Call (Claude 3.5 Haiku)")
    print("=" * 70)
    print()

    api_key = get_api_key("anthropic")
    if not api_key:
        print("  Skipping Anthropic demo (no API key).")
        print()
        print("  Here is what the code looks like:")
        print()
        print('  import anthropic')
        print()
        print('  client = anthropic.Anthropic()  # Uses ANTHROPIC_API_KEY env var')
        print()
        print('  message = client.messages.create(')
        print('      model="claude-3-5-haiku-20241022",')
        print('      max_tokens=300,')
        print('      system="You are a helpful assistant.",')
        print('      messages=[')
        print('          {"role": "user", "content": "What is prompt engineering?"}')
        print('      ]')
        print('  )')
        print()
        print('  print(message.content[0].text)')
        print()
        return

    try:
        import anthropic

        client = anthropic.Anthropic(api_key=api_key)

        print("  Sending request to Claude 3.5 Haiku...")
        start_time = time.time()

        message = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=300,
            system="You are a helpful assistant. Be concise and clear.",
            messages=[
                {
                    "role": "user",
                    "content": "What is prompt engineering? Explain in 3 sentences."
                }
            ],
        )

        elapsed = time.time() - start_time

        # Extract and display the response
        text = message.content[0].text
        usage = message.usage

        print(f"  Response received in {elapsed:.2f} seconds")
        print()
        print(f"  Model: {message.model}")
        print(f"  Response:")
        print(f"  {'-' * 60}")
        for line in text.split("\n"):
            print(f"    {line}")
        print(f"  {'-' * 60}")
        print()
        print(f"  Token Usage:")
        print(f"    Input tokens:  {usage.input_tokens}")
        print(f"    Output tokens: {usage.output_tokens}")

        # Calculate cost (Claude 3.5 Haiku pricing)
        input_cost = (usage.input_tokens / 1_000_000) * 0.80
        output_cost = (usage.output_tokens / 1_000_000) * 4.00
        total_cost = input_cost + output_cost
        print(f"    Estimated cost: ${total_cost:.6f}")
        print()

    except ImportError:
        print("  Error: anthropic package not installed.")
        print("  Install with: pip install anthropic")
        print()
    except Exception as e:
        print(f"  Error: {e}")
        print()


# =============================================================================
# SECTION 3: Streaming Response
# =============================================================================

def demo_streaming():
    """Demonstrate streaming responses (tokens appear as they are generated)."""
    print("=" * 70)
    print("DEMO 3: Streaming Response (OpenAI)")
    print("=" * 70)
    print()

    api_key = get_api_key("openai")
    if not api_key:
        print("  Skipping streaming demo (no API key).")
        print()
        print("  Streaming allows you to display text as it is generated,")
        print("  rather than waiting for the full response.")
        print()
        print("  Code example:")
        print()
        print('  stream = client.chat.completions.create(')
        print('      model="gpt-4o-mini",')
        print('      messages=[{"role": "user", "content": "Tell me a short story."}],')
        print('      stream=True')
        print('  )')
        print()
        print('  for chunk in stream:')
        print('      content = chunk.choices[0].delta.content')
        print('      if content:')
        print('          print(content, end="", flush=True)')
        print()
        return

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)

        print("  Streaming response from GPT-4o mini:")
        print(f"  {'-' * 60}")
        print("    ", end="")

        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": "Write a haiku about artificial intelligence."
                }
            ],
            stream=True,
            max_tokens=100,
        )

        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                print(content, end="", flush=True)

        print()
        print(f"  {'-' * 60}")
        print()
        print("  Notice how text appeared token by token!")
        print("  Streaming improves perceived latency for users.")
        print()

    except ImportError:
        print("  Error: openai package not installed.")
        print()
    except Exception as e:
        print(f"  Error: {e}")
        print()


# =============================================================================
# SECTION 4: Conversation with History
# =============================================================================

def demo_conversation():
    """Demonstrate a multi-turn conversation with message history."""
    print("=" * 70)
    print("DEMO 4: Multi-Turn Conversation (Anthropic)")
    print("=" * 70)
    print()

    api_key = get_api_key("anthropic")
    if not api_key:
        print("  Skipping conversation demo (no API key).")
        print()
        print("  Multi-turn conversations work by sending the full")
        print("  message history with each request:")
        print()
        print("  messages = [")
        print('      {"role": "user", "content": "My name is Alice."},')
        print('      {"role": "assistant", "content": "Hello Alice!"},')
        print('      {"role": "user", "content": "What is my name?"},')
        print("  ]")
        print()
        print("  The model uses the history to maintain context.")
        print()
        return

    try:
        import anthropic

        client = anthropic.Anthropic(api_key=api_key)

        # Build a conversation step by step
        messages = []

        conversation_turns = [
            "My name is Alice and I am learning about AI.",
            "What are the three types of AI we discussed?",
            "Which type of AI are you?",
        ]

        print("  Running a 3-turn conversation with Claude:")
        print()

        for i, user_message in enumerate(conversation_turns, 1):
            messages.append({"role": "user", "content": user_message})

            print(f"  Turn {i} - User: {user_message}")

            response = client.messages.create(
                model="claude-3-5-haiku-20241022",
                max_tokens=200,
                system="You are a friendly AI tutor teaching about artificial intelligence. "
                       "Remember the student's name and previous context.",
                messages=messages,
            )

            assistant_message = response.content[0].text
            messages.append({"role": "assistant", "content": assistant_message})

            print(f"  Turn {i} - Claude: {assistant_message}")
            print()

        print("  Key insight: The model maintains context because we send")
        print("  the full conversation history with each request.")
        print(f"  Total messages sent in final request: {len(messages)}")
        print()

    except ImportError:
        print("  Error: anthropic package not installed.")
        print()
    except Exception as e:
        print(f"  Error: {e}")
        print()


# =============================================================================
# SECTION 5: Comparing Models Side by Side
# =============================================================================

def demo_comparison():
    """Send the same prompt to both OpenAI and Anthropic and compare."""
    print("=" * 70)
    print("DEMO 5: Side-by-Side Model Comparison")
    print("=" * 70)
    print()

    openai_key = get_api_key("openai")
    anthropic_key = get_api_key("anthropic")

    if not openai_key or not anthropic_key:
        print("  Skipping comparison demo (need both API keys).")
        print()
        print("  This demo sends the same prompt to both GPT-4o mini")
        print("  and Claude 3.5 Haiku, then compares the responses,")
        print("  response times, token usage, and costs.")
        print()
        return

    prompt = "Explain the concept of 'attention' in AI transformers in exactly 2 sentences."

    print(f"  Prompt: \"{prompt}\"")
    print()

    results = {}

    # OpenAI
    try:
        from openai import OpenAI

        client = OpenAI(api_key=openai_key)

        start = time.time()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200,
        )
        elapsed = time.time() - start

        results["GPT-4o mini"] = {
            "response": response.choices[0].message.content,
            "time": elapsed,
            "input_tokens": response.usage.prompt_tokens,
            "output_tokens": response.usage.completion_tokens,
            "input_cost_per_1m": 0.15,
            "output_cost_per_1m": 0.60,
        }
    except Exception as e:
        print(f"  OpenAI error: {e}")

    # Anthropic
    try:
        import anthropic

        client = anthropic.Anthropic(api_key=anthropic_key)

        start = time.time()
        message = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=200,
            messages=[{"role": "user", "content": prompt}],
        )
        elapsed = time.time() - start

        results["Claude 3.5 Haiku"] = {
            "response": message.content[0].text,
            "time": elapsed,
            "input_tokens": message.usage.input_tokens,
            "output_tokens": message.usage.output_tokens,
            "input_cost_per_1m": 0.80,
            "output_cost_per_1m": 4.00,
        }
    except Exception as e:
        print(f"  Anthropic error: {e}")

    # Display comparison
    for model_name, data in results.items():
        cost = (
            (data["input_tokens"] / 1_000_000) * data["input_cost_per_1m"]
            + (data["output_tokens"] / 1_000_000) * data["output_cost_per_1m"]
        )

        print(f"  --- {model_name} ---")
        print(f"  Response: {data['response']}")
        print(f"  Time: {data['time']:.2f}s | "
              f"Input: {data['input_tokens']} tokens | "
              f"Output: {data['output_tokens']} tokens | "
              f"Cost: ${cost:.6f}")
        print()


# =============================================================================
# SECTION 6: Error Handling Best Practices
# =============================================================================

def demo_error_handling():
    """Demonstrate proper error handling for API calls."""
    print("=" * 70)
    print("DEMO 6: Error Handling Best Practices")
    print("=" * 70)
    print()

    print("  When making API calls, always handle these errors:")
    print()
    print("  1. AuthenticationError -- Invalid or missing API key")
    print("  2. RateLimitError -- Too many requests")
    print("  3. APIConnectionError -- Network issues")
    print("  4. BadRequestError -- Invalid request parameters")
    print("  5. InternalServerError -- Provider-side issues")
    print()
    print("  Example error handling code:")
    print()

    code = '''
    import anthropic
    from anthropic import (
        APIConnectionError,
        RateLimitError,
        APIStatusError,
    )
    import time

    client = anthropic.Anthropic()

    def call_with_retry(prompt, max_retries=3):
        """Make an API call with automatic retry on transient errors."""
        for attempt in range(max_retries):
            try:
                response = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=500,
                    messages=[{"role": "user", "content": prompt}],
                )
                return response.content[0].text

            except RateLimitError:
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Rate limited. Waiting {wait_time}s...")
                time.sleep(wait_time)

            except APIConnectionError:
                print("Connection error. Retrying...")
                time.sleep(1)

            except APIStatusError as e:
                print(f"API error (status {e.status_code}): {e.message}")
                if e.status_code >= 500:
                    time.sleep(2)  # Server error, retry
                else:
                    raise  # Client error, do not retry

        raise Exception("Max retries exceeded")
    '''

    for line in code.strip().split("\n"):
        print(f"  {line}")
    print()


# =============================================================================
# MAIN
# =============================================================================

def main():
    """Run all demos."""
    print()
    print("  FIRST API CALL -- OpenAI and Anthropic")
    print("  Module 01 - Foundations of Artificial Intelligence")
    print("  Master in Prompt Engineering and AI")
    print()
    print("  Prerequisites:")
    print("    pip install openai anthropic")
    print("    export OPENAI_API_KEY='your-key-here'")
    print("    export ANTHROPIC_API_KEY='your-key-here'")
    print()

    demo_openai_basic()
    demo_anthropic_basic()
    demo_streaming()
    demo_conversation()
    demo_comparison()
    demo_error_handling()

    print("=" * 70)
    print("All demos complete!")
    print()
    print("Next steps:")
    print("  1. Get your API keys from platform.openai.com and console.anthropic.com")
    print("  2. Set them as environment variables")
    print("  3. Run this script again to see live API responses")
    print("  4. Modify the prompts and parameters to experiment")
    print("=" * 70)


if __name__ == "__main__":
    main()
