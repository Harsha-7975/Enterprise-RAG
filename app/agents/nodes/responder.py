from app.agents.state import AgentState
from app.config import Settings
from langchain_groq import ChatGroq
import logfire

llm = ChatGroq(api_key=Settings.GROQ_API_KEY,model = Settings.GROQ_MODEL)

def responder_node(state: AgentState):
    """
    This will give a response based on the user query 
    """
    query = state['current_query']

    history = ""
    for msg in state['messages'][:-1]:
        role = "User" if msg["role"]=="User" else "Assistant"
        history += f"{role} : {msg['content']}\n "

    user_message = state['messages'][-1]['content'] if state['messages'] else ""

    if query == "CONVERSATIONAL":
        logfire.info("Generating conversational response using memory.")
        prompt = f"""
        You are a friendly and helpful Enterprise AI Assistant.
        Answer the user's latest message using the CONVERSATION HISTORY below.

        CONVERSATION HISTORY:
        {history}

        LATEST MESSAGE:
        "{user_message}"
        """
    else:
        logfire.info("Generating technical RAG response.")
        max_context_chars = 25000
        full_context = ""

        for doc in state["documents"]:
            if len(full_context) + len(doc) < max_context_chars:
                full_context += doc + "\n\n"
            else:
                logfire.warning("Context truncated to fit Groq TPM limits.")
                break

        prompt = f"""
        You are a Senior Technical Architect.
        Answer the question using the TECHNICAL CONTEXT provided.

        TECHNICAL CONTEXT:
        {full_context}

        CONVERSATION HISTORY:
        {history}

        USER QUESTION:
        "{user_message}"
        """
    with logfire.span("LLM Synthesis:"):
        try:
            response = llm.invoke(prompt).content
            logfire.info("Response generated successfully!")
            return{
                "final_answer":response,
                "status":"Response generated",
                "plan":state["plan"],
                "messages":[{"role":"assistant","content":response}]
            }
        except Exception as e:
            logfire.error(f"LLM generation failed : {e}")

