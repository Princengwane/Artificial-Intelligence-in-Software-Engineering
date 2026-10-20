#!/usr/bin/python3
"""
Sentiment Analysis Tool
Analyzes the sentiment of a sentence using the Text Processing API.
"""

import os
import sys

import requests


def analyze_sentiment(text):
    """
    Analyze text sentiment using the authenticated Text Processing API.

    Args:
        text (str): The sentence to analyze.

    Returns:
        str | None: The sentiment label (positive, negative, or neutral),
            or None if configuration, network communication, or the response
            is invalid.
    """
    api_key = os.getenv("TEXT_PROCESSING_API_KEY")
    if not api_key:
        print(
            "Error: TEXT_PROCESSING_API_KEY environment variable not set.",
            file=sys.stderr,
        )
        return None

    url = "https://api.text-processing.com/api/sentiment/"
    payload = {"text": text}
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        response = requests.post(
            url,
            data=payload,
            headers=headers,
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, dict):
            raise ValueError("Expected a JSON object")
        label = data.get("label", "neutral")

        if label == "pos":
            return "positive"
        if label == "neg":
            return "negative"
        return "neutral"
    except requests.exceptions.Timeout as e:
        print(
            f"Request timed out while contacting the sentiment API: {e}",
            file=sys.stderr,
        )
        return None
    except requests.exceptions.ConnectionError as e:
        print(
            f"Connection error while contacting the sentiment API: {e}",
            file=sys.stderr,
        )
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}", file=sys.stderr)
        return None
    except (KeyError, ValueError) as e:
        print(f"Invalid response format: {e}", file=sys.stderr)
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}", file=sys.stderr)
        return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./sentiment_analyzer.py <sentence>")
        sys.exit(1)
    sentence = " ".join(sys.argv[1:])
    result = analyze_sentiment(sentence)
    if result:
        print(result)
    else:
        sys.exit(1)
