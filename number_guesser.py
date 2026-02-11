{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMnNI7+AhXiPqcuvtdnFCRk",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/mlambert05/my-first-project/blob/master/Untitled0.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "import time\n",
        "print(\"Guessing time buckerinos, 1 through 100! Take a stab at it\")\n",
        "print(\"picking a number... \")\n",
        "time.sleep(2)\n",
        "guess = int(input(\"Alright now go on guess! \"))\n",
        "correct_number = random.randint(1,100)\n",
        "s = 1\n",
        "\n",
        "while guess != correct_number:\n",
        "  s += 1\n",
        "  if guess < correct_number:\n",
        "    guess = int(input(\"Higherrrr \"))\n",
        "\n",
        "  else:\n",
        "    guess > correct_number\n",
        "    time.sleep(1)\n",
        "    guess = int(input(\"Lower bestie... \"))\n",
        "\n",
        "print(f\"Yippee, {correct_number} is the right number, It took {s} guesses\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0rRYIvjDHiWq",
        "outputId": "e135bc0c-e264-43f1-9d6e-6ddec24a581c"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Guessing time buckerinos, 1 through 100! Take a stab at it\n",
            "picking a number... \n",
            "Alright now go on guess! 50\n",
            "Higherrrr 85\n",
            "Lower bestie... 65\n",
            "Lower bestie... 51\n",
            "Higherrrr 59\n",
            "Lower bestie... 57\n",
            "Lower bestie... 56\n",
            "Lower bestie... 55\n",
            "Yippee, 55 is the right number, It took 8 guesses\n"
          ]
        }
      ]
    }
  ]
}
