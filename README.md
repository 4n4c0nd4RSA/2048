
# 2048 AI Challenge

Welcome to the 2048 AI Challenge, a fun project where enthusiasts can compete to build and train a TensorFlow model to play the game 2048 and achieve the highest score possible. This repository provides the necessary tools and environments for developing, training, competing with, and playing AI models.

## Project Structure

This repository contains the following files:

- `2048 AI.py`: The main Python script to run the AI. By default, it loads `prod_model.keras`. Press ESC to reload the model during execution or use arrow keys to manually play if the model gets stuck.
- `2048.py`: A Python script for a human-playable version of the 2048 game. Enjoy playing 2048 directly through this script.
- `Gym.ipynb`: A Jupyter Notebook used for developing and training the AI models.
- `BattleGround.ipynb`: A Jupyter Notebook for competing models against each other to see which performs best.
- `deploy.bat`: A batch file to copy `dev_model.keras` to `prod_model.keras`, which is the default model loaded by `2048 AI.py`.

## Getting Started

### Prerequisites

Before you can run the scripts, ensure you have the following installed:
- Python 3.x
- TensorFlow
- Keras
- Jupyter Notebook or Jupyter Lab

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/4n4c0nd4RSA/2048.git
cd 2048
```

### Running the AI

To run the AI, navigate to the directory containing `2048 AI.py` and execute the script:

```bash
python "2048 AI.py"
```

To update the production model, run the `deploy.bat` script to copy `prod_model.keras` to the models folder then `dev_model.keras` to `prod_model.keras`.

### Playing the Game

To play the human version of 2048, run:

```bash
python "2048.py"
```

Enjoy the classic game and practice your strategies!

### Training and Competing

Use `Gym.ipynb` to develop and train your models. Once trained, update the development model using the `deploy.bat` script.

Use `BattleGround.ipynb` to pit your trained model against others. Load your models in the notebook and run the competitions to see which model scores the highest.

## Contributing

Contributions to improve the AI or the training/competing environments are welcome. Please fork the repository and submit a pull request with your improvements.

## License

This project is open source and available under the [MIT License](LICENSE.md).

