{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Narendra_Modi_Sentiment_Analysis_100_tweets.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNTE3TyihQB0C6kRNGuB+rU",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/vdnew/Sentiment-Analysis-on-tweet/blob/main/content/narendra_modi_sentiment_analysis_100_tweets.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DwcTay6GuOkk"
      },
      "source": [
        "import tweepy\r\n",
        "import numpy as np\r\n",
        "import pandas as pd\r\n",
        "import re\r\n",
        "from textblob import TextBlob\r\n",
        "from tweepy import OAuthHandler"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gEZZEefRJIAp"
      },
      "source": [
        "consumer_api_key = 'oFteRkiOlYWFcltcsac31k5iy'\r\n",
        "consumer_api_secret = 'U9nKojJYkwza6iZsNGgnhg887hirpOACngI4qX53PfzAAVFQpm' \r\n",
        "access_token = '772357570061332480-fTXprmuuhNnwJSkbGhrbKkcoV0B0wEx'\r\n",
        "access_token_secret ='D3E5bg7oTmEU6JxZUfD9zkNl4hHN85E1uCxfLXpRklq0j'"
      ],
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gwMg0FagJLV6"
      },
      "source": [
        "authorizer = OAuthHandler(consumer_api_key, consumer_api_secret)\r\n",
        "authorizer.set_access_token(access_token, access_token_secret)"
      ],
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kU83WUWJJOnC"
      },
      "source": [
        "api = tweepy.API(authorizer ,timeout=15)"
      ],
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "oopSyBOcJaCV"
      },
      "source": [
        "twitterAccount = \"narendramodi\""
      ],
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GsJLcbF1Jgr1"
      },
      "source": [
        "tweets = tweepy.Cursor(api.user_timeline, \r\n",
        "                        screen_name=twitterAccount, \r\n",
        "                        count=None,\r\n",
        "                        since_id=None,\r\n",
        "                        max_id=None,\r\n",
        "                        trim_user=True,\r\n",
        "                        exclude_replies=True,\r\n",
        "                        contributor_details=False,\r\n",
        "                        include_entities=False\r\n",
        "                        ).items(100);"
      ],
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RRiNiDDaJoPf"
      },
      "source": [
        "df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweet'])"
      ],
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "fniwWD5yJqXY",
        "outputId": "c7585938-bc1c-459e-ec5e-8a4f219b5b41"
      },
      "source": [
        "df.head()"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Tweet</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Centenary celebrations of Chauri Chaura incide...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Glad to see your affection towards India. :)\\n...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>The incident at Chauri Chaura has a special pl...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>RT @MEAIndia: #IndiaTogether \\n#IndiaAgainstPr...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>India offers unlimited potential in defence an...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                                               Tweet\n",
              "0  Centenary celebrations of Chauri Chaura incide...\n",
              "1  Glad to see your affection towards India. :)\\n...\n",
              "2  The incident at Chauri Chaura has a special pl...\n",
              "3  RT @MEAIndia: #IndiaTogether \\n#IndiaAgainstPr...\n",
              "4  India offers unlimited potential in defence an..."
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YLsssvnpJsfw"
      },
      "source": [
        "def cleanUpTweet(txt):\r\n",
        "    # Remove mentions\r\n",
        "    txt = re.sub(r'@[A-Za-z0-9_]+', '', txt)\r\n",
        "    # Remove hashtags\r\n",
        "    txt = re.sub(r'#', '', txt)\r\n",
        "    # Remove retweets:\r\n",
        "    txt = re.sub(r'RT : ', '', txt)\r\n",
        "    # Remove urls\r\n",
        "    txt = re.sub(r'https?:\\/\\/[A-Za-z0-9\\.\\/]+', '', txt)\r\n",
        "    return txt"
      ],
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rFaPeiDmJu7f"
      },
      "source": [
        "df['Tweet'] = df['Tweet'].apply(cleanUpTweet)"
      ],
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "m6B1yBGbJxSh",
        "outputId": "1b4a3ad8-8b6c-449f-926d-13949056d53a"
      },
      "source": [
        "df.head()"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Tweet</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Centenary celebrations of Chauri Chaura incide...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Glad to see your affection towards India. :)\\n...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>The incident at Chauri Chaura has a special pl...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>IndiaTogether \\nIndiaAgainstPropaganda \\n\\n</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>India offers unlimited potential in defence an...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                                               Tweet\n",
              "0  Centenary celebrations of Chauri Chaura incide...\n",
              "1  Glad to see your affection towards India. :)\\n...\n",
              "2  The incident at Chauri Chaura has a special pl...\n",
              "3       IndiaTogether \\nIndiaAgainstPropaganda \\n\\n \n",
              "4  India offers unlimited potential in defence an..."
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "A2DZB4EFJzYD"
      },
      "source": [
        "\r\n",
        "\r\n",
        "def getTextSubjectivity(txt):\r\n",
        "    return TextBlob(txt).sentiment.subjectivity\r\n",
        "\r\n",
        "def getTextPolarity(txt):\r\n",
        "    return TextBlob(txt).sentiment.polarity\r\n",
        "\r\n"
      ],
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "N2d_DtDjKD20"
      },
      "source": [
        "df['Subjectivity'] = df['Tweet'].apply(getTextSubjectivity)\r\n",
        "df['Polarity'] = df['Tweet'].apply(getTextPolarity)"
      ],
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "hyNS8u1dKGXm",
        "outputId": "991dc931-f4af-4fcb-8978-36cbb93d9b7d"
      },
      "source": [
        "df.head()"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Tweet</th>\n",
              "      <th>Subjectivity</th>\n",
              "      <th>Polarity</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Centenary celebrations of Chauri Chaura incide...</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Glad to see your affection towards India. :)\\n...</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.500000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>The incident at Chauri Chaura has a special pl...</td>\n",
              "      <td>0.571429</td>\n",
              "      <td>0.357143</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>IndiaTogether \\nIndiaAgainstPropaganda \\n\\n</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>India offers unlimited potential in defence an...</td>\n",
              "      <td>0.666667</td>\n",
              "      <td>0.366667</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                                               Tweet  Subjectivity  Polarity\n",
              "0  Centenary celebrations of Chauri Chaura incide...      0.000000  0.000000\n",
              "1  Glad to see your affection towards India. :)\\n...      1.000000  0.500000\n",
              "2  The incident at Chauri Chaura has a special pl...      0.571429  0.357143\n",
              "3       IndiaTogether \\nIndiaAgainstPropaganda \\n\\n       0.000000  0.000000\n",
              "4  India offers unlimited potential in defence an...      0.666667  0.366667"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "28kGzBxVKIDR"
      },
      "source": [
        "df = df.drop(df[df['Tweet'] == ''].index)"
      ],
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RBPsg0xyKO4R"
      },
      "source": [
        "\r\n",
        "\r\n",
        "# negative, nautral, positive analysis\r\n",
        "def getTextAnalysis(a):\r\n",
        "    if a < 0:\r\n",
        "        return \"Negative\"\r\n",
        "    elif a == 0:\r\n",
        "        return \"Neutral\"\r\n",
        "    else:\r\n",
        "        return \"Positive\"\r\n",
        "\r\n"
      ],
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "darrcueXKR0c"
      },
      "source": [
        "df['Score'] = df['Polarity'].apply(getTextAnalysis)"
      ],
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "WuEcMmM0KULi",
        "outputId": "473e9359-b768-4657-ae91-a18856af20d5"
      },
      "source": [
        "df.head()"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Tweet</th>\n",
              "      <th>Subjectivity</th>\n",
              "      <th>Polarity</th>\n",
              "      <th>Score</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Centenary celebrations of Chauri Chaura incide...</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>Neutral</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Glad to see your affection towards India. :)\\n...</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.500000</td>\n",
              "      <td>Positive</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>The incident at Chauri Chaura has a special pl...</td>\n",
              "      <td>0.571429</td>\n",
              "      <td>0.357143</td>\n",
              "      <td>Positive</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>IndiaTogether \\nIndiaAgainstPropaganda \\n\\n</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>Neutral</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>India offers unlimited potential in defence an...</td>\n",
              "      <td>0.666667</td>\n",
              "      <td>0.366667</td>\n",
              "      <td>Positive</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                                               Tweet  ...     Score\n",
              "0  Centenary celebrations of Chauri Chaura incide...  ...   Neutral\n",
              "1  Glad to see your affection towards India. :)\\n...  ...  Positive\n",
              "2  The incident at Chauri Chaura has a special pl...  ...  Positive\n",
              "3       IndiaTogether \\nIndiaAgainstPropaganda \\n\\n   ...   Neutral\n",
              "4  India offers unlimited potential in defence an...  ...  Positive\n",
              "\n",
              "[5 rows x 4 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 284
        },
        "id": "7l13Cnj0KWCk",
        "outputId": "57649efd-0285-4631-ef95-00bf2b6eb564"
      },
      "source": [
        "import matplotlib.pyplot as plt\r\n",
        "\r\n",
        "labels = df.groupby('Score').count().index.values\r\n",
        "\r\n",
        "values = df.groupby('Score').size().values\r\n",
        "\r\n",
        "plt.bar(labels, values)"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<BarContainer object of 3 artists>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 19
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "id": "FvBGEsrxKafO",
        "outputId": "0c694642-a752-4dc8-dbf8-7e3ebd7c0c66"
      },
      "source": [
        "for index, row in df.iterrows():\r\n",
        "    if row['Score'] == 'Positive':\r\n",
        "        plt.scatter(row['Polarity'], row['Subjectivity'], color=\"green\")\r\n",
        "    elif row['Score'] == 'Negative':\r\n",
        "        plt.scatter(row['Polarity'], row['Subjectivity'], color=\"red\")\r\n",
        "    elif row['Score'] == 'Neutral':\r\n",
        "        plt.scatter(row['Polarity'], row['Subjectivity'], color=\"blue\")\r\n",
        "\r\n",
        "plt.title('Twitter Sentiment Analysis')\r\n",
        "plt.xlabel('Polarity')\r\n",
        "plt.ylabel('Subjectivity')\r\n",
        "# add legend\r\n",
        "plt.show()"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PyWeKWrGKoS1",
        "outputId": "8f5232dc-a579-4576-f118-ce13774fae2b"
      },
      "source": [
        "\r\n",
        "\r\n",
        "objective = df[df['Subjectivity'] == 0]\r\n",
        "\r\n",
        "print(str(objective.shape[0]/(df.shape[0])*100) + \" % of objective tweets\")\r\n",
        "\r\n"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "45.0 % of objective tweets\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 269
        },
        "id": "dZCz-kCpKqtL",
        "outputId": "54fca2ba-3453-450f-9b5b-e85a8b72ce60"
      },
      "source": [
        "from wordcloud import WordCloud\r\n",
        "words = ' '.join([tweet for tweet in df['Tweet']])\r\n",
        "wordCloud = WordCloud(width=600, height=400).generate(words)\r\n",
        "\r\n",
        "plt.imshow(wordCloud)\r\n",
        "plt.show()"
      ],
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Vqxm9ppGRsMa"
      },
      "source": [
        "from sklearn.preprocessing import LabelEncoder"
      ],
      "execution_count": 23,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "SoB2jF-vRsn7",
        "outputId": "aea6ddcc-997b-4e0b-d6c4-b69fe86cfe7b"
      },
      "source": [
        "df.head()"
      ],
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Tweet</th>\n",
              "      <th>Subjectivity</th>\n",
              "      <th>Polarity</th>\n",
              "      <th>Score</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Centenary celebrations of Chauri Chaura incide...</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>Neutral</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Glad to see your affection towards India. :)\\n...</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.500000</td>\n",
              "      <td>Positive</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>The incident at Chauri Chaura has a special pl...</td>\n",
              "      <td>0.571429</td>\n",
              "      <td>0.357143</td>\n",
              "      <td>Positive</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>IndiaTogether \\nIndiaAgainstPropaganda \\n\\n</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>Neutral</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>India offers unlimited potential in defence an...</td>\n",
              "      <td>0.666667</td>\n",
              "      <td>0.366667</td>\n",
              "      <td>Positive</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                                               Tweet  ...     Score\n",
              "0  Centenary celebrations of Chauri Chaura incide...  ...   Neutral\n",
              "1  Glad to see your affection towards India. :)\\n...  ...  Positive\n",
              "2  The incident at Chauri Chaura has a special pl...  ...  Positive\n",
              "3       IndiaTogether \\nIndiaAgainstPropaganda \\n\\n   ...   Neutral\n",
              "4  India offers unlimited potential in defence an...  ...  Positive\n",
              "\n",
              "[5 rows x 4 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PSsmUx7xS2vR",
        "outputId": "c6ccc1bb-0f35-4428-c28c-319ecf101ec1"
      },
      "source": [
        "from nltk.stem.porter import PorterStemmer\r\n",
        "import nltk \r\n",
        "import nltk.corpus\r\n",
        "from nltk.corpus import stopwords\r\n",
        "from nltk.tokenize import BlanklineTokenizer\r\n",
        "from nltk.tokenize import TweetTokenizer\r\n",
        "nltk.download('punkt')\r\n",
        "nltk.download('wordnet')\r\n",
        "nltk.download('stopwords')\r\n",
        "from nltk.stem import WordNetLemmatizer\r\n",
        "import string"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[nltk_data] Downloading package punkt to /root/nltk_data...\n",
            "[nltk_data]   Package punkt is already up-to-date!\n",
            "[nltk_data] Downloading package wordnet to /root/nltk_data...\n",
            "[nltk_data]   Package wordnet is already up-to-date!\n",
            "[nltk_data] Downloading package stopwords to /root/nltk_data...\n",
            "[nltk_data]   Package stopwords is already up-to-date!\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0WPpuIItS608"
      },
      "source": [
        "ps = PorterStemmer() #pour \"text preprocessing\"\r\n",
        "\r\n",
        "message = []\r\n",
        "\r\n",
        "for i in range(0, df.shape[0]):\r\n",
        "    #accepter que les mots alphabétiques\r\n",
        "    review = re.sub('[^a-zA-Z]', ' ', df['Tweet'][i])\r\n",
        "    #convertir tous minuscule\r\n",
        "    review = review.lower()\r\n",
        "    #splitter chaque ligne\r\n",
        "    review = review.split()\r\n",
        "    #\r\n",
        "    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]\r\n",
        "    #construire de nouveau la ligne\r\n",
        "    review = ' '.join(review)\r\n",
        "    message.append(review)"
      ],
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8eaZa4xKS8bI"
      },
      "source": [
        "message\r\n",
        "data = df"
      ],
      "execution_count": 27,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 500
        },
        "id": "9J3x1WpDT8Bn",
        "outputId": "0991ce74-3527-43b4-820b-ade98ecb636e"
      },
      "source": [
        "data['clean_text']=np.empty((len(message),1))\r\n",
        "for i in range(len(message)):\r\n",
        "    data['clean_text'][i]=message[i]\r\n",
        "data['clean_text_len']=data['clean_text'].apply(len)\r\n",
        "data.head()"
      ],
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py:3: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  This is separate from the ipykernel package so we can avoid doing imports until\n",
            "/usr/local/lib/python3.6/dist-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  iloc._setitem_with_indexer(indexer, value)\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Tweet</th>\n",
              "      <th>Subjectivity</th>\n",
              "      <th>Polarity</th>\n",
              "      <th>Score</th>\n",
              "      <th>clean_text</th>\n",
              "      <th>clean_text_len</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Centenary celebrations of Chauri Chaura incide...</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>Neutral</td>\n",
              "      <td>centenari celebr chauri chaura incid</td>\n",
              "      <td>36</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Glad to see your affection towards India. :)\\n...</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.500000</td>\n",
              "      <td>Positive</td>\n",
              "      <td>glad see affect toward india believ world fami...</td>\n",
              "      <td>63</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>The incident at Chauri Chaura has a special pl...</td>\n",
              "      <td>0.571429</td>\n",
              "      <td>0.357143</td>\n",
              "      <td>Positive</td>\n",
              "      <td>incid chauri chaura special place histori free...</td>\n",
              "      <td>78</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>IndiaTogether \\nIndiaAgainstPropaganda \\n\\n</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>Neutral</td>\n",
              "      <td>indiatogeth indiaagainstpropaganda</td>\n",
              "      <td>34</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>India offers unlimited potential in defence an...</td>\n",
              "      <td>0.666667</td>\n",
              "      <td>0.366667</td>\n",
              "      <td>Positive</td>\n",
              "      <td>india offer unlimit potenti defenc aerospac ae...</td>\n",
              "      <td>79</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                                               Tweet  ...  clean_text_len\n",
              "0  Centenary celebrations of Chauri Chaura incide...  ...              36\n",
              "1  Glad to see your affection towards India. :)\\n...  ...              63\n",
              "2  The incident at Chauri Chaura has a special pl...  ...              78\n",
              "3       IndiaTogether \\nIndiaAgainstPropaganda \\n\\n   ...              34\n",
              "4  India offers unlimited potential in defence an...  ...              79\n",
              "\n",
              "[5 rows x 6 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 293
        },
        "id": "BWS12ib9UpI7",
        "outputId": "a1c94ec4-624c-4b9c-8cb5-bfcb3a0d7520"
      },
      "source": [
        "data.head()"
      ],
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Tweet</th>\n",
              "      <th>Subjectivity</th>\n",
              "      <th>Polarity</th>\n",
              "      <th>Score</th>\n",
              "      <th>clean_text</th>\n",
              "      <th>clean_text_len</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Centenary celebrations of Chauri Chaura incide...</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>Neutral</td>\n",
              "      <td>centenari celebr chauri chaura incid</td>\n",
              "      <td>36</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Glad to see your affection towards India. :)\\n...</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.500000</td>\n",
              "      <td>Positive</td>\n",
              "      <td>glad see affect toward india believ world fami...</td>\n",
              "      <td>63</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>The incident at Chauri Chaura has a special pl...</td>\n",
              "      <td>0.571429</td>\n",
              "      <td>0.357143</td>\n",
              "      <td>Positive</td>\n",
              "      <td>incid chauri chaura special place histori free...</td>\n",
              "      <td>78</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>IndiaTogether \\nIndiaAgainstPropaganda \\n\\n</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>Neutral</td>\n",
              "      <td>indiatogeth indiaagainstpropaganda</td>\n",
              "      <td>34</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>India offers unlimited potential in defence an...</td>\n",
              "      <td>0.666667</td>\n",
              "      <td>0.366667</td>\n",
              "      <td>Positive</td>\n",
              "      <td>india offer unlimit potenti defenc aerospac ae...</td>\n",
              "      <td>79</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                                               Tweet  ...  clean_text_len\n",
              "0  Centenary celebrations of Chauri Chaura incide...  ...              36\n",
              "1  Glad to see your affection towards India. :)\\n...  ...              63\n",
              "2  The incident at Chauri Chaura has a special pl...  ...              78\n",
              "3       IndiaTogether \\nIndiaAgainstPropaganda \\n\\n   ...              34\n",
              "4  India offers unlimited potential in defence an...  ...              79\n",
              "\n",
              "[5 rows x 6 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QL0mZLdIUqnQ"
      },
      "source": [
        "from sklearn.feature_extraction.text import CountVectorizer\r\n",
        "cv = CountVectorizer(max_features=15000)\r\n",
        "X1 = cv.fit_transform(message).toarray()"
      ],
      "execution_count": 30,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VMVb_fQlUunH",
        "outputId": "0822b6bf-641c-4966-c529-e4be7ce9ae62"
      },
      "source": [
        "X1.shape"
      ],
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(100, 520)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 597
        },
        "id": "IvZOSZ5jUwyt",
        "outputId": "f1f49855-afcb-49d7-9ad1-cd37319ca4a6"
      },
      "source": [
        "X2 = data.copy()\r\n",
        "X2"
      ],
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Tweet</th>\n",
              "      <th>Subjectivity</th>\n",
              "      <th>Polarity</th>\n",
              "      <th>Score</th>\n",
              "      <th>clean_text</th>\n",
              "      <th>clean_text_len</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Centenary celebrations of Chauri Chaura incide...</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>Neutral</td>\n",
              "      <td>centenari celebr chauri chaura incid</td>\n",
              "      <td>36</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Glad to see your affection towards India. :)\\n...</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.500000</td>\n",
              "      <td>Positive</td>\n",
              "      <td>glad see affect toward india believ world fami...</td>\n",
              "      <td>63</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>The incident at Chauri Chaura has a special pl...</td>\n",
              "      <td>0.571429</td>\n",
              "      <td>0.357143</td>\n",
              "      <td>Positive</td>\n",
              "      <td>incid chauri chaura special place histori free...</td>\n",
              "      <td>78</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>IndiaTogether \\nIndiaAgainstPropaganda \\n\\n</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>Neutral</td>\n",
              "      <td>indiatogeth indiaagainstpropaganda</td>\n",
              "      <td>34</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>India offers unlimited potential in defence an...</td>\n",
              "      <td>0.666667</td>\n",
              "      <td>0.366667</td>\n",
              "      <td>Positive</td>\n",
              "      <td>india offer unlimit potenti defenc aerospac ae...</td>\n",
              "      <td>79</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>95</th>\n",
              "      <td>On National Girl Child Day, we salute our Desh...</td>\n",
              "      <td>0.375000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>Neutral</td>\n",
              "      <td>nation girl child day salut deshkibeti accompl...</td>\n",
              "      <td>77</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>96</th>\n",
              "      <td>Thank you Prime Minister ! Our fight against C...</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>Neutral</td>\n",
              "      <td>thank prime minist fight covid share effort</td>\n",
              "      <td>43</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>97</th>\n",
              "      <td>Some glimpses from the programme at Victoria M...</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>Neutral</td>\n",
              "      <td>glimps programm victoria memori parakramdiva</td>\n",
              "      <td>44</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>98</th>\n",
              "      <td>জাতীয় গ্রন্থাগার কলকাতার অন্যতম একটি দর্শনীয়...</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>Neutral</td>\n",
              "      <td>parakramdiva</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>99</th>\n",
              "      <td>আমি পশ্চিম বঙ্গের এই মহৎ ভূমি কে প্রণাম জানাই।</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>Neutral</td>\n",
              "      <td></td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>100 rows × 6 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "                                                Tweet  ...  clean_text_len\n",
              "0   Centenary celebrations of Chauri Chaura incide...  ...              36\n",
              "1   Glad to see your affection towards India. :)\\n...  ...              63\n",
              "2   The incident at Chauri Chaura has a special pl...  ...              78\n",
              "3        IndiaTogether \\nIndiaAgainstPropaganda \\n\\n   ...              34\n",
              "4   India offers unlimited potential in defence an...  ...              79\n",
              "..                                                ...  ...             ...\n",
              "95  On National Girl Child Day, we salute our Desh...  ...              77\n",
              "96  Thank you Prime Minister ! Our fight against C...  ...              43\n",
              "97  Some glimpses from the programme at Victoria M...  ...              44\n",
              "98  জাতীয় গ্রন্থাগার কলকাতার অন্যতম একটি দর্শনীয়...  ...              12\n",
              "99    আমি পশ্চিম বঙ্গের এই মহৎ ভূমি কে প্রণাম জানাই।   ...               0\n",
              "\n",
              "[100 rows x 6 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VC44yjhMUyvH"
      },
      "source": [
        "X2.drop(['Tweet','clean_text'],axis=1,inplace=True)"
      ],
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Oncz0m3wU0gK"
      },
      "source": [
        "X3 = pd.DataFrame(data=X1)"
      ],
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RxuQ44r7Vf-V",
        "outputId": "6e7af513-89c1-4289-e11a-b245f001fb8d"
      },
      "source": [
        "X3.shape"
      ],
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(100, 520)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9YxQiTZgVhX-"
      },
      "source": [
        "X4 = pd.concat([X2,X3],axis=1)"
      ],
      "execution_count": 38,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "X-yGvg_SVl2w"
      },
      "source": [
        "X4.shape\r\n",
        "X4.drop(['Score'], axis=1, inplace=True)"
      ],
      "execution_count": 49,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3VF2dM5WV62D"
      },
      "source": [
        "y = data.Score\r\n",
        "y = y.replace({'negative' : 0 , 'neutral' : 1 , 'positive' : 2})"
      ],
      "execution_count": 50,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Sy7a3HtxVnQD"
      },
      "source": [
        "from sklearn.model_selection import train_test_split\r\n",
        "x_train,x_test,y_train,y_test = train_test_split(X4,y,test_size=0.2,random_state=42)"
      ],
      "execution_count": 51,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Y3oEdoa0VsR7"
      },
      "source": [
        "import pickle"
      ],
      "execution_count": 52,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3GCGZ9BfWKMc"
      },
      "source": [
        "filename = 'GBK_Model1.sav'\r\n",
        "loaded_model = pickle.load(open(filename, 'rb'))"
      ],
      "execution_count": 53,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hMurJK2SWSHV",
        "outputId": "48253973-2e17-4b9b-8b3d-9103bb0ab37c"
      },
      "source": [
        "loaded_model.fit(x_train, y_train)"
      ],
      "execution_count": 55,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "GradientBoostingClassifier(ccp_alpha=0.0, criterion='friedman_mse', init=None,\n",
              "                           learning_rate=0.1, loss='deviance', max_depth=3,\n",
              "                           max_features=None, max_leaf_nodes=None,\n",
              "                           min_impurity_decrease=0.0, min_impurity_split=None,\n",
              "                           min_samples_leaf=1, min_samples_split=100,\n",
              "                           min_weight_fraction_leaf=0.0, n_estimators=100,\n",
              "                           n_iter_no_change=None, presort='deprecated',\n",
              "                           random_state=42, subsample=1.0, tol=0.0001,\n",
              "                           validation_fraction=0.1, verbose=0,\n",
              "                           warm_start=False)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 55
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0nDqPjd-WbVU",
        "outputId": "345cd17f-b60f-462f-daf5-400184348fc7"
      },
      "source": [
        "loaded_model.score(x_test, y_test)"
      ],
      "execution_count": 57,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.4"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 57
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5_7DZCRrXW-U",
        "outputId": "fb2313e1-e21c-412b-8a7a-a8ef6150a470"
      },
      "source": [
        "loaded_model.predict(x_test)"
      ],
      "execution_count": 61,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['Neutral', 'Neutral', 'Neutral', 'Neutral', 'Neutral', 'Neutral',\n",
              "       'Neutral', 'Neutral', 'Neutral', 'Neutral', 'Neutral', 'Neutral',\n",
              "       'Neutral', 'Neutral', 'Neutral', 'Neutral', 'Neutral', 'Neutral',\n",
              "       'Neutral', 'Neutral'], dtype=object)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 61
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "N2GIBOjsW_NX"
      },
      "source": [
        "# Saving New Version of Model\r\n",
        "filename = 'GBK_Model_2.sav'\r\n",
        "pickle.dump(loaded_model, open(filename, 'wb'))"
      ],
      "execution_count": 58,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UNtHSna5XU31"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}