using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        string text = "The quick brown fox jumps over the lazy fox and sees another fox";
        string wordToFind = "fox";
        WordIndexFinder(wordToFind, text);
    }

    static void WordIndexFinder(string wordToFind, string text)
    {
        string[] words = text.Split(' ');
        List<int> indices = new List<int>();

        for (int index = 0; index < words.Length; index++)
        {
            if (words[index] == wordToFind)
            {
                indices.Add(index);
            }
        }

        if (indices.Count > 0)
        {
            Console.WriteLine($"The word '{wordToFind}' is found at indices: {string.Join(", ", indices)}");
        }
        else
        {
            Console.WriteLine($"The word '{wordToFind}' is not in the list.");
        }
    }
}


