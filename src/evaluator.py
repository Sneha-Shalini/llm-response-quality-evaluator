import pandas as pd
import re

class LLMResponseEvaluator:
    def __init__(self):
        self.rubric = ['helpfulness', 'truthfulness', 'coherence', 'harmlessness']
    
    def check_hallucination(self, text):
        """Simple hallucination flags"""
        red_flags = ["as an ai", "as a language model", "i don't have access to real-time", "knowledge cutoff"]
        return any(flag in text.lower() for flag in red_flags)
    
    def score_response(self, prompt, response):
        scores = {}
        # Helpfulness: based on length and relevance
        scores['helpfulness'] = 5 if len(response.split()) > 40 else 3
        # Truthfulness: penalize if hallucination flag
        scores['truthfulness'] = 2 if self.check_hallucination(response) else 5
        # Coherence: check repetition
        scores['coherence'] = 5 if len(set(response.split())) > len(response.split())*0.7 else 3
        # Harmlessness
        scores['harmlessness'] = 5  # extend with toxicity check
        
        scores['hallucination'] = self.check_hallucination(response)
        scores['total'] = sum([scores['helpfulness'], scores['truthfulness'], scores['coherence']])
        return scores

    def compare(self, prompt, response_a, response_b):
        score_a = self.score_response(prompt, response_a)
        score_b = self.score_response(prompt, response_b)
        winner = 'A' if score_a['total'] > score_b['total'] else 'B'
        return {'winner': winner, 'score_a': score_a, 'score_b': score_b}

# Demo
if __name__ == "__main__":
    eval = LLMResponseEvaluator()
    prompt = "Explain quantum computing in simple terms"
    a = "Quantum computing uses qubits which can be 0 and 1 at same time. As an AI I don't have real-time data but..."
    b = "Quantum computing uses quantum bits or qubits. Unlike normal bits that are 0 or 1, qubits can exist in both states simultaneously (superposition), allowing faster computation for certain problems like cryptography and drug discovery."
    result = eval.compare(prompt, a, b)
    print(result)
