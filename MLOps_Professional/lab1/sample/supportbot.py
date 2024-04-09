# supportbot business logic

def get_suppport(text:str):
    """_summary_

    Parameters
    ----------
    text : str
        text prompt from the user that determine the response of the supportbot

    Returns
    -------
    str
        Text response from the supportbot based on the user's prompt
    """

    response = "bring the harvester in for maintenance" if text.lower() == "help" else "support on this not available yet"

    return response