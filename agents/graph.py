from langgraph.graph import Graph, END, START

from extractor import extractor
from reader import reader
from validator import validator

def human_call(data):
    """
    Function to handle human feedback.
    This function asks the user for input based on the provided data.
    
    Args:
        data: The data to be processed or evaluated by the human.

    Returns:
        str: The decision made by the human (e.g., "continue" or "human").
    """
    print("Human feedback required.")
    print(f"Data received for review: {data}")

    while True:
        decision = input("What would you like to do? (continue/human): ").strip().lower()
        
        if decision in ["continue", "human"]:
            return decision
        else:
            print("Invalid input. Please enter 'continue' or 'human'.")

def reader_should_continue(validation_result):
    """
    Function to determine if the workflow should continue based on validation results.
    
    Args:
        validation_result: The result from the validator (True/False).

    Returns:
        str: 'continue' if the workflow should continue,
             'human' if human intervention is needed.
    """
    return "continue" if validation_result else "human"

def create_workflow():
    # Initialize the workflow graph
    workflow = Graph()
    
    # Add nodes to the workflow
    workflow.add_node("reader", reader)
    workflow.add_node("extractor", extractor)
    workflow.add_node("validator", validator)
    workflow.add_node("human_call", human_call)

    # Define the workflow edges
    workflow.add_edge(START, "reader")
    workflow.add_edge("reader", "extractor")  # reader should be the starting point
    workflow.add_edge("extractor", "validator")
    
    # Add conditional routing based on the validator's output
    workflow.add_conditional_edges(
        "validator",
        reader_should_continue,
        {
            "human": "human_call",
            "continue": END,
        }
    )
    
    # Connect the human call back to the extractor
    workflow.add_edge("human_call", "extractor")
    
    # Compile the workflow
    return workflow.compile()