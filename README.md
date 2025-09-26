# NextWordPro

NextWordPro is a **Next Word Prediction** project built in Python with a **Tkinter-based GUI**.  
It allows users to input a sequence of words and predicts the most likely next word using a trained language model.

---

## 🚀 Features
- Interactive GUI built with **Tkinter**  
- Predicts the next word for a given text input  
- Pre-trained tokenizer included (`tokenizer1.pkl`)  
- Training and evaluation notebooks available (`.ipynb`)  
- Multiple implementations (`predictions.py`, `predictions2.py`) for flexibility  

---

## 📊 Model Training
- **Dataset**: The model was trained on *metamorphosis_clean.txt*  
- **Training Details**:  
  - Trained for **150 epochs**  
  - Loss reduced from **7.87 â†’ 0.62**  
  - Framework: TensorFlow/Keras  

This demonstrates the modelâ€™s ability to learn meaningful language patterns for next-word prediction.

---

## ⚡ Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/sankhalabhavik18-max/NextWordPro.git
cd NextWordPro
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the GUI
```bash
python predictions.py
```
or
```bash
python predictions2.py
```

### 4. Explore the Notebooks
For training and evaluation details, open the Jupyter notebooks:
- `Next Word Prediction-1.ipynb`  
- `Predictions-1.ipynb`  

---

## 📂 Repository Structure
```
NextWordPro/
â”‚-- predictions.py            # GUI + model prediction
â”‚-- predictions2.py           # Alternate implementation
â”‚-- tokenizer1.pkl            # Pre-trained tokenizer
â”‚-- metamorphosis_clean.txt   # Training dataset
â”‚-- Next Word Prediction-1.ipynb
â”‚-- Predictions-1.ipynb
â”‚-- requirements.txt          # Dependencies
â”‚-- README.md                 # Project documentation
```

---

## 📌 Future Improvements
- Add support for **top-3 / top-5 predictions**  
- Improve GUI layout and user experience  
- Expand dataset for broader vocabulary coverage  
- Experiment with advanced architectures such as LSTMs with embeddings or Transformers  

---

## 🙌 Acknowledgements
- Python & Tkinter for the GUI  
- TensorFlow/Keras for model training  
- Dataset: *metamorphosis_clean.txt* (Project Gutenberg source text)  
