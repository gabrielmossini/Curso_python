{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "TrianguloRetangulo.py",
      "provenance": [],
      "authorship_tag": "ABX9TyNToHqfjA4xlcbwMFs4nWuV",
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
        "<a href=\"https://colab.research.google.com/github/gamossini/Curso_python/blob/main/TrianguloRetangulo.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Write a function that tests whether a traingle of 3 sides is a right triangle. \n",
        "Since we could not control the order the sides that user gives us (such that c is the longest length), \n",
        "we need to need to manually check if c is the longest length (length a and b can be any order). \n",
        "Otherwise, our Pythagorean Theorem will failed. \n"
      ],
      "metadata": {
        "id": "nPpgBg1bHBrX"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "SXrqnMPpG2j6"
      },
      "outputs": [],
      "source": [
        "def isTriangulo(a, b, c):\n",
        "  if(max(a,b,c) != c):\n",
        "\n",
        "    tmp = c\n",
        "    c = max(a,b,c)\n",
        "\n",
        "    if a == c:\n",
        "      a = tmp\n",
        "    elif b == c:\n",
        "      b = tmp\n",
        "\n",
        "  if a**2 + b **2 == c**2:\n",
        "    print(\"É um triângulo Retângulo\")\n",
        "    return True\n",
        "    print(\"NÃO é um triângulo Retângulo\")\n",
        "    return False\n",
        "\n",
        "def main():\n",
        "    a = input(\"Digite o valor de A do triângulo: \")\n",
        "    b = input(\"Digite o valor de B do triângulo: \")\n",
        "    c = input(\"Digite o valor de C do triângulo: \")\n",
        "    \n",
        "    return isTriangulo(int(a), int(b), int(c))\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()"
      ]
    }
  ]
}