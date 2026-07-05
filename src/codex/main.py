import os
import argparse
import json
from openai import OpenAI
from dotenv import load_dotenv
import sys



from .prompts import system_prompt
from .call_function import call_function

from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file


CODEX_BANNER = r"""
   ______          __    _  __
  / ____/___  ____/ /___| |/ /
 / /   / __ \/ __  / _ \  / / 
/ /___/ /_/ / /_/ /  __// _ \ 
\____/\____/\__,_/\___/_/ |_| 
"""

CODEX_TAGLINE = "  Your autonomous coding agent. Reads. Writes. Runs. Fixes."

CODEX_CAPABILITIES = """
  What I can do:
    explore  ->  Browse your project directory
    read     ->  Read any file in your workspace
    write    ->  Create or rewrite code files
    run      ->  Execute Python scripts & tests

  Try: codex "who are you?"
"""

def create_parser():
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        prog="codex",
        description="CodeX AI - An intelligent coding assistant powered by AI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  codex "list all files in the calculator directory"
  codex "read main.py and explain it"
  codex "create a new file called test.py with hello world"
  codex --verbose "run the test suite"
        """
    )
    
    parser.add_argument(
        "prompt",
        type=str,
        nargs="?",
        help="The task or question for the AI agent"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output showing all iterations"
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )
    
    return parser


def main():
    import sys
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
        
    CYAN   = "\033[96m"
    BOLD   = "\033[1m"
    DIM    = "\033[2m"
    RESET  = "\033[0m"
    YELLOW = "\033[93m"
    print(CYAN + BOLD + CODEX_BANNER + RESET)
    print(YELLOW + BOLD + CODEX_TAGLINE + RESET)
    print(DIM + CODEX_CAPABILITIES + RESET)
    
    parser = create_parser()
    args = parser.parse_args()
    
    # Handle no prompt provided
    if not args.prompt:
        parser.print_help()
        return
    
    user_prompt = args.prompt


    # =========================
    # STEP 1: Load API key
    # =========================
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("ERROR: OPENROUTER_API_KEY environment variable not set")
        print("Please set your API key in a .env file or export it")
        sys.exit(1)

    client = OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
    )

    # =========================
    # STEP 2: Prepare messages (OpenAI format)
    # =========================
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    # =========================
    # STEP 3: Tools (schemas only)
    # =========================
    tools = [
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ]

    # =========================
    # STEP 4: Agent Loop (up to 20 iterations)
    # =========================
    max_iterations = 20
    for iteration in range(max_iterations):
        if args.verbose:
            print(f"\n--- Iteration {iteration + 1} ---")

        # Call the model
        response = client.chat.completions.create(
            model="nvidia/nemotron-3-nano-30b-a3b:free",
            messages=messages,
            tools=tools,
            tool_choice="auto",
            temperature=0,
        )

        message = response.choices[0].message

        # Add the assistant's response to messages
        assistant_message = {
            "role": "assistant",
            "content": message.content or "",
        }
        
        if message.tool_calls:
            assistant_message["tool_calls"] = [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {
                        "name": tc.function.name,
                        "arguments": tc.function.arguments,
                    }
                }
                for tc in message.tool_calls
            ]
        
        messages.append(assistant_message)

        # =========================
        # STEP 5: Handle tool calls
        # =========================
        if message.tool_calls:
            tool_results = []

            for tool_call in message.tool_calls:
                function_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)

                if args.verbose:
                    print(f"Calling function: {function_name}({arguments})")
                else:
                    print(f" - {function_name}")

                function_result = call_function(
                    {
                        "name": function_name,
                        "arguments": arguments,
                    },
                    verbose=args.verbose,
                )

                # Print the tool result directly (for run_python_file output)
                result_content = function_result["result"]
                if result_content and not args.verbose:
                    print(result_content)

                tool_results.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": function_name,
                    "content": result_content,
                })

            # Add all tool results to messages
            for tool_result in tool_results:
                messages.append(tool_result)

        else:
            # No tool calls - model has finished
            print("Final response:")
            print(message.content)
            break

    else:
        # Loop ended without a final response
        print("ERROR: Maximum iterations reached without a final response from the model.")
        exit(1)


if __name__ == "__main__":
    main()

