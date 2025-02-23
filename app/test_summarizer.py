import pytest
import os
from app.summarizer import MedicalTextSummarizer

# Define paths
NOTES_DIR = "notes/stroke_notes"
RESULTS_DIR = "test_results"

# Ensure results directory exists
os.makedirs(RESULTS_DIR, exist_ok=True)

def read_notes():
    """Read all note files from the directory and return their content."""
    note_files = [f for f in os.listdir(NOTES_DIR) if f.endswith(".txt")]
    notes = []
    
    for file in note_files:
        with open(os.path.join(NOTES_DIR, file), "r", encoding="utf-8") as f:
            notes.append((file, f.read()))
    
    return notes

@pytest.mark.parametrize("filename, note_text", read_notes())
def test_summarizer(filename, note_text):
    """Test summarizer on all note files and store results."""
    summarizer = MedicalTextSummarizer()
    
    summary = summarizer.summarize(note_text)

    # Save the result in the test_results folder
    result_file = os.path.join(RESULTS_DIR, f"summary_{filename}")
    with open(result_file, "w", encoding="utf-8") as f:
        f.write(summary)

    print(f"\nStored summary for {filename} in {result_file}")
    
    assert isinstance(summary, str) and len(summary) > 0

def test_invalid_input():
    summarizer = MedicalTextSummarizer()
    with pytest.raises(ValueError):
        summarizer.summarize("")