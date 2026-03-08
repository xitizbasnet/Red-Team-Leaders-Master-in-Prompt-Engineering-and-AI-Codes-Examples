"""
Complete OpenAI Fine-Tuning Workflow
=====================================

This script provides a complete workflow for fine-tuning OpenAI models,
including: file upload, job creation, monitoring, testing, and evaluation.

Requirements:
    pip install openai python-dotenv tiktoken

Usage:
    1. Set OPENAI_API_KEY in .env or environment
    2. Prepare your training data as JSONL (see fine-tuning-data-preparation.py)
    3. Run: python fine-tuning-openai-example.py

Author: Master in Prompt Engineering and AI - Module 05
"""

import os
import sys
import time
import json
from typing import Optional, List, Dict
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# =============================================================================
# STEP 1: FILE UPLOAD
# =============================================================================

def upload_file(file_path: str, purpose: str = "fine-tune") -> str:
    """
    Upload a JSONL file to OpenAI for fine-tuning.

    Args:
        file_path: Path to the JSONL file
        purpose: File purpose (default: "fine-tune")

    Returns:
        File ID string
    """
    print(f"Uploading {file_path}...")

    with open(file_path, "rb") as f:
        response = client.files.create(file=f, purpose=purpose)

    print(f"  File ID:    {response.id}")
    print(f"  Filename:   {response.filename}")
    print(f"  Size:       {response.bytes:,} bytes")
    print(f"  Status:     {response.status}")
    print(f"  Created:    {response.created_at}")

    return response.id


def list_uploaded_files():
    """List all uploaded fine-tuning files."""
    files = client.files.list(purpose="fine-tune")

    print("\nUploaded Fine-Tuning Files:")
    print("-" * 70)
    for f in files.data:
        print(f"  {f.id} | {f.filename:30s} | {f.bytes:>10,} bytes | {f.status}")
    print()


# =============================================================================
# STEP 2: CREATE FINE-TUNING JOB
# =============================================================================

def create_job(
    training_file_id: str,
    model: str = "gpt-4o-mini-2024-07-18",
    validation_file_id: Optional[str] = None,
    suffix: Optional[str] = None,
    n_epochs: Optional[int] = None,
    batch_size: Optional[int] = None,
    learning_rate_multiplier: Optional[float] = None,
) -> str:
    """
    Create a fine-tuning job.

    Args:
        training_file_id: ID of the uploaded training file
        model: Base model to fine-tune
        validation_file_id: Optional validation file ID
        suffix: Custom suffix for the fine-tuned model name
        n_epochs: Number of training epochs (None = auto)
        batch_size: Training batch size (None = auto)
        learning_rate_multiplier: LR multiplier (None = auto)

    Returns:
        Job ID string
    """
    print(f"\nCreating fine-tuning job...")
    print(f"  Base model:     {model}")
    print(f"  Training file:  {training_file_id}")

    # Build parameters
    params = {
        "training_file": training_file_id,
        "model": model,
    }

    if validation_file_id:
        params["validation_file"] = validation_file_id
        print(f"  Validation file: {validation_file_id}")

    if suffix:
        params["suffix"] = suffix
        print(f"  Suffix:         {suffix}")

    # Hyperparameters
    hyperparams = {}
    if n_epochs is not None:
        hyperparams["n_epochs"] = n_epochs
        print(f"  Epochs:         {n_epochs}")
    if batch_size is not None:
        hyperparams["batch_size"] = batch_size
        print(f"  Batch size:     {batch_size}")
    if learning_rate_multiplier is not None:
        hyperparams["learning_rate_multiplier"] = learning_rate_multiplier
        print(f"  LR multiplier:  {learning_rate_multiplier}")

    if hyperparams:
        params["hyperparameters"] = hyperparams

    # Create the job
    job = client.fine_tuning.jobs.create(**params)

    print(f"\n  Job created!")
    print(f"  Job ID:         {job.id}")
    print(f"  Status:         {job.status}")
    print(f"  Created at:     {job.created_at}")

    return job.id


# =============================================================================
# STEP 3: MONITOR JOB
# =============================================================================

def monitor_job(job_id: str, poll_interval: int = 30) -> Optional[str]:
    """
    Monitor a fine-tuning job until completion.

    Args:
        job_id: The fine-tuning job ID
        poll_interval: Seconds between status checks

    Returns:
        Fine-tuned model name (or None if failed)
    """
    print(f"\nMonitoring job {job_id}...")
    print(f"Polling every {poll_interval} seconds.\n")

    seen_events = set()

    while True:
        # Get job status
        job = client.fine_tuning.jobs.retrieve(job_id)

        # Print status
        status_line = f"[{time.strftime('%H:%M:%S')}] Status: {job.status}"
        if job.trained_tokens:
            status_line += f" | Trained tokens: {job.trained_tokens:,}"
        print(status_line)

        # Print new events
        try:
            events = client.fine_tuning.jobs.list_events(
                fine_tuning_job_id=job_id, limit=20
            )
            for event in reversed(events.data):
                event_key = f"{event.created_at}_{event.message}"
                if event_key not in seen_events:
                    seen_events.add(event_key)
                    print(f"  Event: {event.message}")
        except Exception:
            pass

        # Check terminal states
        if job.status == "succeeded":
            print(f"\n{'='*50}")
            print(f"FINE-TUNING SUCCEEDED!")
            print(f"{'='*50}")
            print(f"Fine-tuned model: {job.fine_tuned_model}")
            print(f"Trained tokens:   {job.trained_tokens:,}")
            return job.fine_tuned_model

        elif job.status == "failed":
            print(f"\n{'='*50}")
            print(f"FINE-TUNING FAILED")
            print(f"{'='*50}")
            if job.error:
                print(f"Error code:    {job.error.code}")
                print(f"Error message: {job.error.message}")
            return None

        elif job.status == "cancelled":
            print(f"\nFine-tuning was cancelled.")
            return None

        time.sleep(poll_interval)


def get_job_status(job_id: str):
    """Get the current status of a fine-tuning job."""
    job = client.fine_tuning.jobs.retrieve(job_id)

    print(f"\nJob: {job.id}")
    print(f"  Status:           {job.status}")
    print(f"  Model:            {job.model}")
    print(f"  Fine-tuned model: {job.fine_tuned_model or 'N/A'}")
    print(f"  Created:          {job.created_at}")
    print(f"  Trained tokens:   {job.trained_tokens or 'N/A'}")

    if job.error:
        print(f"  Error:            {job.error.message}")

    return job


def list_jobs(limit: int = 10):
    """List recent fine-tuning jobs."""
    jobs = client.fine_tuning.jobs.list(limit=limit)

    print(f"\nRecent Fine-Tuning Jobs:")
    print("-" * 80)
    for job in jobs.data:
        model_name = job.fine_tuned_model or "N/A"
        print(f"  {job.id} | {job.status:12s} | {job.model:25s} | {model_name}")
    print()


# =============================================================================
# STEP 4: TEST THE FINE-TUNED MODEL
# =============================================================================

def test_model(
    model_name: str,
    messages: List[Dict],
    temperature: float = 0.1,
    max_tokens: int = 500
) -> str:
    """
    Test a fine-tuned model with a set of messages.

    Args:
        model_name: Name of the fine-tuned model
        messages: Chat messages to send
        temperature: Generation temperature
        max_tokens: Maximum response tokens

    Returns:
        Model's response text
    """
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return response.choices[0].message.content


def run_test_suite(model_name: str, test_cases: List[Dict]):
    """
    Run a suite of tests against a fine-tuned model.

    Args:
        model_name: Name of the fine-tuned model
        test_cases: List of dicts with 'messages' and optional 'description'
    """
    print(f"\nRunning {len(test_cases)} tests on {model_name}...")
    print("=" * 60)

    for i, test in enumerate(test_cases, 1):
        description = test.get("description", f"Test {i}")
        messages = test["messages"]

        print(f"\n--- {description} ---")
        print(f"User: {messages[-1]['content'][:100]}...")

        try:
            response = test_model(model_name, messages)
            print(f"Response: {response[:300]}...")
        except Exception as e:
            print(f"Error: {e}")

    print("\n" + "=" * 60)


# =============================================================================
# STEP 5: COMPARE BASE VS. FINE-TUNED
# =============================================================================

def compare_models(
    base_model: str,
    fine_tuned_model: str,
    test_messages: List[Dict],
    label: str = "Test"
):
    """
    Compare outputs from base and fine-tuned models side by side.
    """
    print(f"\n{'='*60}")
    print(f"COMPARISON: {label}")
    print(f"{'='*60}")
    print(f"User: {test_messages[-1]['content']}")

    # Base model
    print(f"\n--- Base Model ({base_model}) ---")
    try:
        base_response = test_model(base_model, test_messages)
        print(base_response[:400])
    except Exception as e:
        print(f"Error: {e}")
        base_response = ""

    # Fine-tuned model
    print(f"\n--- Fine-Tuned Model ({fine_tuned_model}) ---")
    try:
        ft_response = test_model(fine_tuned_model, test_messages)
        print(ft_response[:400])
    except Exception as e:
        print(f"Error: {e}")
        ft_response = ""

    print()
    return base_response, ft_response


# =============================================================================
# STEP 6: EVALUATION
# =============================================================================

def evaluate_response(
    question: str,
    response: str,
    expected: Optional[str] = None,
    criteria: Optional[List[str]] = None,
) -> Dict:
    """
    Use GPT-4o to evaluate a fine-tuned model's response.

    Returns:
        Dict with scores and explanation
    """
    criteria = criteria or [
        "format_compliance",
        "tone_appropriateness",
        "content_accuracy",
        "helpfulness",
        "professionalism"
    ]

    criteria_text = "\n".join(f"- {c}: Rate 1-5" for c in criteria)

    eval_prompt = f"""Evaluate this AI assistant response.

QUESTION: {question}

RESPONSE: {response}

{f'EXPECTED BEHAVIOR: {expected}' if expected else ''}

Rate each criterion on a scale of 1-5:
{criteria_text}

Return valid JSON with the structure:
{{"scores": {{{", ".join(f'"{c}": <1-5>' for c in criteria)}}}, "overall": <1-5>, "notes": "<brief notes>"}}"""

    eval_response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": eval_prompt}],
        temperature=0.0,
        response_format={"type": "json_object"},
    )

    try:
        return json.loads(eval_response.choices[0].message.content)
    except json.JSONDecodeError:
        return {"scores": {}, "overall": 0, "notes": "Failed to parse evaluation"}


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def cancel_job(job_id: str):
    """Cancel a running fine-tuning job."""
    client.fine_tuning.jobs.cancel(job_id)
    print(f"Cancellation requested for job {job_id}")


def delete_model(model_name: str):
    """Delete a fine-tuned model."""
    client.models.delete(model_name)
    print(f"Deleted model: {model_name}")


def delete_file(file_id: str):
    """Delete an uploaded file."""
    client.files.delete(file_id)
    print(f"Deleted file: {file_id}")


# =============================================================================
# COMPLETE WORKFLOW EXAMPLE
# =============================================================================

def run_complete_workflow(
    training_file: str,
    validation_file: Optional[str] = None,
    model: str = "gpt-4o-mini-2024-07-18",
    suffix: str = "my-model",
    wait_for_completion: bool = True,
):
    """
    Run the complete fine-tuning workflow from start to finish.

    Args:
        training_file: Path to training JSONL file
        validation_file: Optional path to validation JSONL file
        model: Base model to fine-tune
        suffix: Model name suffix
        wait_for_completion: Whether to wait for training to finish
    """
    print("=" * 60)
    print("  OPENAI FINE-TUNING WORKFLOW")
    print("=" * 60)

    # Step 1: Upload files
    print("\n--- Step 1: Upload Files ---")
    train_file_id = upload_file(training_file)

    val_file_id = None
    if validation_file and os.path.exists(validation_file):
        val_file_id = upload_file(validation_file)

    # Step 2: Create job
    print("\n--- Step 2: Create Fine-Tuning Job ---")
    job_id = create_job(
        training_file_id=train_file_id,
        model=model,
        validation_file_id=val_file_id,
        suffix=suffix,
    )

    # Step 3: Monitor
    if wait_for_completion:
        print("\n--- Step 3: Monitor Training ---")
        fine_tuned_model = monitor_job(job_id)

        if fine_tuned_model:
            # Step 4: Test
            print("\n--- Step 4: Test Fine-Tuned Model ---")
            test_cases = [
                {
                    "description": "Basic support query",
                    "messages": [
                        {"role": "system", "content": "You are a helpful customer support agent."},
                        {"role": "user", "content": "My order hasn't arrived yet."}
                    ]
                },
                {
                    "description": "Technical troubleshooting",
                    "messages": [
                        {"role": "system", "content": "You are a helpful customer support agent."},
                        {"role": "user", "content": "My laptop keeps crashing when I open Chrome."}
                    ]
                },
            ]
            run_test_suite(fine_tuned_model, test_cases)

            print(f"\nFine-tuned model is ready: {fine_tuned_model}")
            print("You can now use it in your applications.")
    else:
        print(f"\nJob {job_id} submitted. Use monitor_job('{job_id}') to track progress.")

    return job_id


# =============================================================================
# MAIN
# =============================================================================

def main():
    """Main entry point with usage examples."""
    print("OpenAI Fine-Tuning Workflow Script")
    print("=" * 40)

    if not os.getenv("OPENAI_API_KEY"):
        print("\nError: OPENAI_API_KEY not set.")
        print("Set it in your environment or .env file.")
        return

    # Show available commands
    print("\nAvailable functions:")
    print("  upload_file(path)                - Upload training data")
    print("  create_job(file_id, model, ...)  - Start fine-tuning")
    print("  monitor_job(job_id)              - Monitor progress")
    print("  test_model(model, messages)      - Test the model")
    print("  compare_models(base, ft, msgs)   - Compare base vs fine-tuned")
    print("  list_jobs()                      - List recent jobs")
    print("  list_uploaded_files()            - List uploaded files")
    print("  run_complete_workflow(file, ...)  - Run entire pipeline")
    print()
    print("Example usage:")
    print('  run_complete_workflow("train.jsonl", suffix="customer-support")')
    print()

    # If training file exists, offer to run
    if os.path.exists("sample_training_data.jsonl"):
        print("Found sample_training_data.jsonl")
        print("To start fine-tuning, call:")
        print('  run_complete_workflow("sample_training_data.jsonl")')
    else:
        print("No training file found.")
        print("Run fine-tuning-data-preparation.py first to create one.")


if __name__ == "__main__":
    main()
