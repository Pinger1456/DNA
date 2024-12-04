# DNA Animation

This project creates a simple ASCII animation of a DNA double-helix. The animation continuously loops, displaying the two strands of DNA with random bases (A, T, C, G). The program uses Python and runs in the terminal.

## Features

- Displays a scrolling DNA double-helix animation.
- Randomly generates DNA bases (A, T, C, G) in the animation.
- Configurable speed of animation via the `PAUSE` parameter.
- Uses Python's built-in libraries: `random`, `time`, and `sys`.

## Requirements

- Python 3.x
- No external dependencies required.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dna-animation.git
   cd dna-animation
   ```

2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the DNA animation:

```bash
python main.py
```

You can modify the speed of the animation by changing the `PAUSE` value in the `config.py` file. The animation continues until you stop it by pressing `Ctrl+C`.

## Testing

To run the unit tests:

1. Install `pytest` if you don't have it already:
   ```bash
   pip install pytest
   ```

2. Run the tests:
   ```bash
   pytest tests/
   ```

## Project Structure

```
project/
│
├── main.py              # Main program to run the animation
├── config.py            # Configuration file with parameters like PAUSE
├── dna.py               # DNA animation logic
├── requirements.txt     # List of dependencies (currently empty)
└── tests/
    └── test_dna.py      # Unit tests for the DNA animation
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by the ASCII art animations from [Al Sweigart's Big Book of Small Python Projects](https://nostarch.com/big-book-small-python-programming).
- Thank you to the contributors who helped improve the project.
