"""
Deek AI Intent Detection
Version: 0.3
"""

def detect_intent(question):

    question = question.lower()

    # Search
    if any(word in question for word in [
        "latest", "today", "news", "weather",
        "current", "live", "recent"
    ]):
        return "SEARCH"

    # Calculator
    if any(word in question for word in [
        "calculate", "+", "-", "*", "/", "×"
    ]):
        return "CALCULATOR"

    # Phone
    if any(word in question for word in [
        "call", "dial"
    ]):
        return "PHONE"

    # Message
    if any(word in question for word in [
        "message", "sms", "text", "send"
    ]):
        return "MESSAGE"

    # Apps
    if any(word in question for word in [
        "open", "launch", "start"
    ]):
        return "APP"

    # Memory
    if any(word in question for word in [
        "remember", "forget", "my name"
    ]):
        return "MEMORY"

    return "CHAT"
