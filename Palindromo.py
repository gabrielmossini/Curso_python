{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Palindromo.py",
      "provenance": [],
      "authorship_tag": "ABX9TyOjdTOy+WLYh1LGGFv9Itr4",
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
        "<a href=\"https://colab.research.google.com/github/gamossini/Curso_python/blob/main/Palindromo.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Determine if the user input is a palindrome. \n",
        "\n",
        "Palindrome: If a word/sentence is spelled the same way when it is reversed. \n",
        "  EX: racecar\n",
        "\n",
        "In order to write this program, we will set a few specifications:\n",
        "  - Treat capitalized letters as lowercase\n",
        "  - Ignore all white spaces and punctuations\n",
        "  - An empty sentence/string IS consider to be a palindrome. "
      ],
      "metadata": {
        "id": "yreQ0moDOEDA"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NUNt11UxOCW5",
        "outputId": "c2387f9a-dc16-44fd-d4a3-3b9b69fe7b90"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite uma palavra:Socorram me subi no onibus em Marrocos\n",
            "Socorram me subi no onibus em Marrocos é um Palindromo\n"
          ]
        }
      ],
      "source": [
        "import string\n",
        "\n",
        "def Palindromo(str):\n",
        "\n",
        "  exclude = set(string.punctuation)\n",
        "  str = ''.join(ch for ch in str if ch not in exclude)\n",
        "  str = str.replace(\" \", \"\").lower()\n",
        "\n",
        "  if str == str[::-1]:\n",
        "    return True\n",
        "  else:\n",
        "    return False\n",
        "\n",
        "def main():\n",
        "  Palavra = input(\"Digite uma palavra:\")\n",
        "\n",
        "  if (Palindromo(Palavra)):\n",
        "    print(Palavra + \" é um Palindromo\")\n",
        "  else:\n",
        "    print(Palavra + \" NÃO é um Palindromo\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "  main()"
      ]
    }
  ]
}