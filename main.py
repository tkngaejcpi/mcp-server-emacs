import os
import shutil
import subprocess

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Emacs")

lookup_emacs_function_script = os.path.join(os.getcwd(), "lookup-emacs-function.el")
lookup_emacs_variable_script = os.path.join(os.getcwd(), "lookup-emacs-variable.el")

def get_emacs_executable():
    return shutil.which("emacs")

@mcp.tool()
def is_emacs_available() -> bool:
    """
    Return if Emacs is available in current environment.

    Returns:
        True if available, False otherwise.
    """
    
    return get_emacs_executable() != None

@mcp.tool()
def lookup_emacs_function(function_name: str) -> str:
    """
    Return the documentation of the given function in Emacs lisp.

    Args:
        function_name: The name of the function.

    Returns:
        The string of the documentation, or a message.
    """
    
    emacs_exec = get_emacs_executable()

    if emacs_exec == None:
        return "Emacs is not available."
    
    result = subprocess.run([
        emacs_exec,
        "--script",
        lookup_emacs_function_script,
        function_name
    ], check=True, capture_output=True, text=True)


    stripped_result =  "\n".join(result.stderr.split("\n")[1:])

    return stripped_result

@mcp.tool()
def lookup_emacs_variable(variable_name: str) -> str:
    """
    Return the documentation of the given variable in Emacs lisp.

    Args:
        variable_name: The name of the variable.

    Returns:
        The string of the documentation, or a message.
    """
    
    emacs_exec = get_emacs_executable()

    if emacs_exec == None:
        return "Emacs is not available."
    
    result = subprocess.run([
        emacs_exec,
        "--script",
        lookup_emacs_variable_script,
        variable_name
    ],  check=True, capture_output=True, text=True)

    stripped_result =  "\n".join(result.stderr.split("\n")[1:])

    return stripped_result

if __name__ == "__main__":
    mcp.run()
