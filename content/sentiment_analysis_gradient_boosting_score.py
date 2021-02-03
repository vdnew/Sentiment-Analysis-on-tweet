{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "kernelspec": {
      "language": "python",
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "pygments_lexer": "ipython3",
      "nbconvert_exporter": "python",
      "version": "3.6.4",
      "file_extension": ".py",
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "name": "python",
      "mimetype": "text/x-python"
    },
    "colab": {
      "name": "Sentiment_Analysis_Gradient_Boosting_Score.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
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
        "<a href=\"https://colab.research.google.com/github/vdnew/Sentiment-Analysis-on-tweet/blob/main/content/sentiment_analysis_gradient_boosting_score.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5iapzfg-KbJx",
        "trusted": true
      },
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import seaborn as sns \n",
        "import matplotlib.pyplot as plt"
      ],
      "execution_count": 91,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OqD1Kyp4KzAJ",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fdf587e9-3d35-4813-dbc5-f3c5d3746c0d"
      },
      "source": [
        "import nltk \n",
        "import nltk.corpus\n",
        "from nltk.corpus import stopwords\n",
        "from nltk.tokenize import BlanklineTokenizer\n",
        "from nltk.tokenize import TweetTokenizer\n",
        "nltk.download('punkt')\n",
        "nltk.download('wordnet')\n",
        "nltk.download('stopwords')\n",
        "from nltk.stem import WordNetLemmatizer\n",
        "import string"
      ],
      "execution_count": 92,
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
        "id": "dEJ9CJvCK-ql",
        "trusted": true
      },
      "source": [
        "import re\n",
        "from nltk.tokenize import word_tokenize\n",
        "import gensim\n",
        "from keras.preprocessing.text import Tokenizer"
      ],
      "execution_count": 93,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4lE11theLG6f",
        "trusted": true
      },
      "source": [
        "from nltk.stem import PorterStemmer \n",
        "from wordcloud import WordCloud\n",
        "from sklearn.model_selection import train_test_split"
      ],
      "execution_count": 94,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RbsZx1-OLOJV",
        "trusted": true
      },
      "source": [
        "dataset = pd.read_csv('/content/Tweets.csv')"
      ],
      "execution_count": 95,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nHL6vPYLLep7",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 452
        },
        "outputId": "81933979-27d5-45c2-bcc5-120904290f2f"
      },
      "source": [
        "dataset.head()"
      ],
      "execution_count": 96,
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
              "      <th>tweet_id</th>\n",
              "      <th>airline_sentiment</th>\n",
              "      <th>airline_sentiment_confidence</th>\n",
              "      <th>negativereason</th>\n",
              "      <th>negativereason_confidence</th>\n",
              "      <th>airline</th>\n",
              "      <th>airline_sentiment_gold</th>\n",
              "      <th>name</th>\n",
              "      <th>negativereason_gold</th>\n",
              "      <th>retweet_count</th>\n",
              "      <th>text</th>\n",
              "      <th>tweet_coord</th>\n",
              "      <th>tweet_created</th>\n",
              "      <th>tweet_location</th>\n",
              "      <th>user_timezone</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>570306133677760513</td>\n",
              "      <td>neutral</td>\n",
              "      <td>1.0000</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Virgin America</td>\n",
              "      <td>NaN</td>\n",
              "      <td>cairdin</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica What @dhepburn said.</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2015-02-24 11:35:52 -0800</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Eastern Time (US &amp; Canada)</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>570301130888122368</td>\n",
              "      <td>positive</td>\n",
              "      <td>0.3486</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0.0000</td>\n",
              "      <td>Virgin America</td>\n",
              "      <td>NaN</td>\n",
              "      <td>jnardino</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica plus you've added commercials t...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2015-02-24 11:15:59 -0800</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Pacific Time (US &amp; Canada)</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>570301083672813571</td>\n",
              "      <td>neutral</td>\n",
              "      <td>0.6837</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Virgin America</td>\n",
              "      <td>NaN</td>\n",
              "      <td>yvonnalynn</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica I didn't today... Must mean I n...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2015-02-24 11:15:48 -0800</td>\n",
              "      <td>Lets Play</td>\n",
              "      <td>Central Time (US &amp; Canada)</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>570301031407624196</td>\n",
              "      <td>negative</td>\n",
              "      <td>1.0000</td>\n",
              "      <td>Bad Flight</td>\n",
              "      <td>0.7033</td>\n",
              "      <td>Virgin America</td>\n",
              "      <td>NaN</td>\n",
              "      <td>jnardino</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica it's really aggressive to blast...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2015-02-24 11:15:36 -0800</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Pacific Time (US &amp; Canada)</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>570300817074462722</td>\n",
              "      <td>negative</td>\n",
              "      <td>1.0000</td>\n",
              "      <td>Can't Tell</td>\n",
              "      <td>1.0000</td>\n",
              "      <td>Virgin America</td>\n",
              "      <td>NaN</td>\n",
              "      <td>jnardino</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica and it's a really big bad thing...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2015-02-24 11:14:45 -0800</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Pacific Time (US &amp; Canada)</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "             tweet_id  ...               user_timezone\n",
              "0  570306133677760513  ...  Eastern Time (US & Canada)\n",
              "1  570301130888122368  ...  Pacific Time (US & Canada)\n",
              "2  570301083672813571  ...  Central Time (US & Canada)\n",
              "3  570301031407624196  ...  Pacific Time (US & Canada)\n",
              "4  570300817074462722  ...  Pacific Time (US & Canada)\n",
              "\n",
              "[5 rows x 15 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 96
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-IwocnoMLf13",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d209965e-8a17-45a5-ff96-de6443464956"
      },
      "source": [
        "dataset.shape"
      ],
      "execution_count": 97,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(14640, 15)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 97
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "54I0WJXjLidb",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ed78cca7-bb5e-4101-b5f3-850c9f1daedf"
      },
      "source": [
        "dataset.airline_sentiment.value_counts()"
      ],
      "execution_count": 98,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "negative    9178\n",
              "neutral     3099\n",
              "positive    2363\n",
              "Name: airline_sentiment, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 98
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TZMhbpyBL0TC",
        "trusted": true
      },
      "source": [
        "#notre objectif est de prédicter la valeur de la colonne \"airlaine_sentiment\""
      ],
      "execution_count": 99,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GsnoCvsTL_EL",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "9f5f8ed8-5366-4a12-b3c7-7066e8d5425f"
      },
      "source": [
        "dataset.info()"
      ],
      "execution_count": 100,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 14640 entries, 0 to 14639\n",
            "Data columns (total 15 columns):\n",
            " #   Column                        Non-Null Count  Dtype  \n",
            "---  ------                        --------------  -----  \n",
            " 0   tweet_id                      14640 non-null  int64  \n",
            " 1   airline_sentiment             14640 non-null  object \n",
            " 2   airline_sentiment_confidence  14640 non-null  float64\n",
            " 3   negativereason                9178 non-null   object \n",
            " 4   negativereason_confidence     10522 non-null  float64\n",
            " 5   airline                       14640 non-null  object \n",
            " 6   airline_sentiment_gold        40 non-null     object \n",
            " 7   name                          14640 non-null  object \n",
            " 8   negativereason_gold           32 non-null     object \n",
            " 9   retweet_count                 14640 non-null  int64  \n",
            " 10  text                          14640 non-null  object \n",
            " 11  tweet_coord                   1019 non-null   object \n",
            " 12  tweet_created                 14640 non-null  object \n",
            " 13  tweet_location                9907 non-null   object \n",
            " 14  user_timezone                 9820 non-null   object \n",
            "dtypes: float64(2), int64(2), object(11)\n",
            "memory usage: 1.7+ MB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "I23_bdgjMG30",
        "trusted": true
      },
      "source": [
        "# les colonnes \"airline_sentiment_gold \" et \"negativereason_gold\" ont trop peu de valeurs non nulles\n",
        "#donc on va les supprimer"
      ],
      "execution_count": 101,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "K9EdRCSOMbO8",
        "trusted": true
      },
      "source": [
        "dataset.drop(['airline_sentiment_gold','negativereason_gold'],axis=1,inplace=True)"
      ],
      "execution_count": 102,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1F2rQ2u6MmIO",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "57fb3d07-dc58-4486-ddd8-4c4cf4242ed4"
      },
      "source": [
        "dataset.tweet_coord.nunique()"
      ],
      "execution_count": 103,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "832"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 103
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aWboGq7BM9i2",
        "trusted": true
      },
      "source": [
        "#parmi 1019 valeurs non nulles du colonne 'tweet_coord' ilya 832 valeurs uniques\n",
        "#donc c'est une colonne peu important"
      ],
      "execution_count": 104,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AKaaWdaKNWtM",
        "trusted": true
      },
      "source": [
        "dataset.drop(['tweet_coord'],axis=1,inplace=True)"
      ],
      "execution_count": 105,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9YX1bzDcN29T",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "742dd353-4ed6-4064-d23c-79235c2a950e"
      },
      "source": [
        "dataset.info()"
      ],
      "execution_count": 106,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 14640 entries, 0 to 14639\n",
            "Data columns (total 12 columns):\n",
            " #   Column                        Non-Null Count  Dtype  \n",
            "---  ------                        --------------  -----  \n",
            " 0   tweet_id                      14640 non-null  int64  \n",
            " 1   airline_sentiment             14640 non-null  object \n",
            " 2   airline_sentiment_confidence  14640 non-null  float64\n",
            " 3   negativereason                9178 non-null   object \n",
            " 4   negativereason_confidence     10522 non-null  float64\n",
            " 5   airline                       14640 non-null  object \n",
            " 6   name                          14640 non-null  object \n",
            " 7   retweet_count                 14640 non-null  int64  \n",
            " 8   text                          14640 non-null  object \n",
            " 9   tweet_created                 14640 non-null  object \n",
            " 10  tweet_location                9907 non-null   object \n",
            " 11  user_timezone                 9820 non-null   object \n",
            "dtypes: float64(2), int64(2), object(8)\n",
            "memory usage: 1.3+ MB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5q3HyZ49N_xm",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "9533799f-21eb-4a7d-f4a8-ae1d47ce46be"
      },
      "source": [
        "dataset.negativereason.value_counts()"
      ],
      "execution_count": 107,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Customer Service Issue         2910\n",
              "Late Flight                    1665\n",
              "Can't Tell                     1190\n",
              "Cancelled Flight                847\n",
              "Lost Luggage                    724\n",
              "Bad Flight                      580\n",
              "Flight Booking Problems         529\n",
              "Flight Attendant Complaints     481\n",
              "longlines                       178\n",
              "Damaged Luggage                  74\n",
              "Name: negativereason, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 107
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "frzEWEiAOEq0",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a2f587f8-9f63-47a8-82e5-6c1865fe944f"
      },
      "source": [
        "dataset.negativereason.nunique()"
      ],
      "execution_count": 108,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "10"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 108
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pkzJxmxyOOVL",
        "trusted": true
      },
      "source": [
        "#trés bien il ya que 10 valeurs uniques"
      ],
      "execution_count": 109,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mdKsBNZyOSks",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6626bf82-671c-48e9-d9a5-0491de991d20"
      },
      "source": [
        "nr = dataset.negativereason.unique()\n",
        "nr"
      ],
      "execution_count": 110,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([nan, 'Bad Flight', \"Can't Tell\", 'Late Flight',\n",
              "       'Customer Service Issue', 'Flight Booking Problems',\n",
              "       'Lost Luggage', 'Flight Attendant Complaints', 'Cancelled Flight',\n",
              "       'Damaged Luggage', 'longlines'], dtype=object)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 110
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fPc9tMvTOZK7",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "afcfa02f-5241-4695-8942-fcffa01349df"
      },
      "source": [
        "nr.reshape(1,11)"
      ],
      "execution_count": 111,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[nan, 'Bad Flight', \"Can't Tell\", 'Late Flight',\n",
              "        'Customer Service Issue', 'Flight Booking Problems',\n",
              "        'Lost Luggage', 'Flight Attendant Complaints',\n",
              "        'Cancelled Flight', 'Damaged Luggage', 'longlines']], dtype=object)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 111
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Oebf8JNHOg8u",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "58904ca9-df9d-4781-a07f-630fc12e40a6"
      },
      "source": [
        "nr[0]"
      ],
      "execution_count": 112,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "nan"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 112
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SufImvwAOqzF",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "outputId": "e7e7f89e-d1f5-4132-b2aa-9ca0287e4f76"
      },
      "source": [
        "nr[5]"
      ],
      "execution_count": 113,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'Flight Booking Problems'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 113
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "39GI_GOsOsjv",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "bafd8d04-4bd8-4eb1-99d6-1880c9932dbc"
      },
      "source": [
        "dataset.negativereason.iloc[0] = 'Bad Flight'"
      ],
      "execution_count": 114,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  iloc._setitem_with_indexer(indexer, value)\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BAdPMGT0PfO4",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "outputId": "e2a982bc-a407-4bab-e321-844dba04c159"
      },
      "source": [
        "dataset.negativereason.iloc[0]"
      ],
      "execution_count": 115,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'Bad Flight'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 115
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4A6qcI_nQX18",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "960eee9f-3ba8-4411-e2e2-56a1999190f7"
      },
      "source": [
        "dataset.negativereason.iloc[1] is np.NaN"
      ],
      "execution_count": 116,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 116
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FXrzxRrtPso9",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6a2afe2e-098a-4ded-96a5-266f0ff7aeba"
      },
      "source": [
        "import random\n",
        "for k in range (dataset.shape[0]):\n",
        "  if dataset.negativereason.iloc[k] is np.NaN:\n",
        "    p = random.randint(1, 10)\n",
        "    dataset.negativereason.iloc[k] = nr[p]"
      ],
      "execution_count": 117,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  iloc._setitem_with_indexer(indexer, value)\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tFx9yORpRMpq",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "21b97929-217c-4fae-8657-9b3f3a9b8ac2"
      },
      "source": [
        "dataset.info()"
      ],
      "execution_count": 118,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 14640 entries, 0 to 14639\n",
            "Data columns (total 12 columns):\n",
            " #   Column                        Non-Null Count  Dtype  \n",
            "---  ------                        --------------  -----  \n",
            " 0   tweet_id                      14640 non-null  int64  \n",
            " 1   airline_sentiment             14640 non-null  object \n",
            " 2   airline_sentiment_confidence  14640 non-null  float64\n",
            " 3   negativereason                14640 non-null  object \n",
            " 4   negativereason_confidence     10522 non-null  float64\n",
            " 5   airline                       14640 non-null  object \n",
            " 6   name                          14640 non-null  object \n",
            " 7   retweet_count                 14640 non-null  int64  \n",
            " 8   text                          14640 non-null  object \n",
            " 9   tweet_created                 14640 non-null  object \n",
            " 10  tweet_location                9907 non-null   object \n",
            " 11  user_timezone                 9820 non-null   object \n",
            "dtypes: float64(2), int64(2), object(8)\n",
            "memory usage: 1.3+ MB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2jAhK3uARPAW",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5d2f5820-8e46-4e95-b6fd-5d65b4e97965"
      },
      "source": [
        "#on va vérifier le résultat\n",
        "dataset.negativereason.value_counts()"
      ],
      "execution_count": 119,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Customer Service Issue         3492\n",
              "Late Flight                    2194\n",
              "Can't Tell                     1713\n",
              "Cancelled Flight               1412\n",
              "Lost Luggage                   1287\n",
              "Bad Flight                     1127\n",
              "Flight Booking Problems        1054\n",
              "Flight Attendant Complaints    1001\n",
              "longlines                       717\n",
              "Damaged Luggage                 643\n",
              "Name: negativereason, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 119
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "f00vFz-jRgMA",
        "trusted": true
      },
      "source": [
        "#trés bien"
      ],
      "execution_count": 120,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KSTq01R_RiXB",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "73e0445e-2e34-479c-9429-02e30a7bb240"
      },
      "source": [
        "dataset.negativereason_confidence.nunique()"
      ],
      "execution_count": 121,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1410"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 121
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cgxQ8pElR35m",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d797defa-da2d-473f-b4df-3a3c73f8ecbe"
      },
      "source": [
        "#1410 valeurs se répétent dans 10522 lignes donc on va les utiliser pour remplacer les valeurs 'NaN'\n",
        "nr = dataset.negativereason_confidence.unique()\n",
        "len(nr)"
      ],
      "execution_count": 122,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1411"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 122
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FOaL-NFWUW-T",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "014c9b66-3659-4f20-e350-d5cf2e92ba3f"
      },
      "source": [
        "nr.reshape(1,1411)"
      ],
      "execution_count": 123,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[   nan, 0.    , 0.7033, ..., 0.6234, 0.644 , 0.7255]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 123
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4fHH4rDEUzG9",
        "trusted": true
      },
      "source": [
        "dataset.negativereason_confidence = dataset.negativereason_confidence.astype('object')"
      ],
      "execution_count": 124,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gJeBIkTmU8tX",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fc7c2374-41ca-4261-ff98-889c4f01091d"
      },
      "source": [
        "dataset.info()"
      ],
      "execution_count": 125,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 14640 entries, 0 to 14639\n",
            "Data columns (total 12 columns):\n",
            " #   Column                        Non-Null Count  Dtype  \n",
            "---  ------                        --------------  -----  \n",
            " 0   tweet_id                      14640 non-null  int64  \n",
            " 1   airline_sentiment             14640 non-null  object \n",
            " 2   airline_sentiment_confidence  14640 non-null  float64\n",
            " 3   negativereason                14640 non-null  object \n",
            " 4   negativereason_confidence     10522 non-null  object \n",
            " 5   airline                       14640 non-null  object \n",
            " 6   name                          14640 non-null  object \n",
            " 7   retweet_count                 14640 non-null  int64  \n",
            " 8   text                          14640 non-null  object \n",
            " 9   tweet_created                 14640 non-null  object \n",
            " 10  tweet_location                9907 non-null   object \n",
            " 11  user_timezone                 9820 non-null   object \n",
            "dtypes: float64(1), int64(2), object(9)\n",
            "memory usage: 1.3+ MB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jp6Pjrl9Sa-4",
        "trusted": true
      },
      "source": [
        "for k in range (dataset.shape[0]):\n",
        "  if dataset.negativereason_confidence.iloc[k] is np.NaN:\n",
        "    p = random.randint(1, 1411)\n",
        "    dataset.negativereason_confidence.iloc[k] = nr[p]"
      ],
      "execution_count": 126,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "i7rGic_EUeu3",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2792580d-c092-4106-867b-f60aad684968"
      },
      "source": [
        "dataset.info()"
      ],
      "execution_count": 127,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 14640 entries, 0 to 14639\n",
            "Data columns (total 12 columns):\n",
            " #   Column                        Non-Null Count  Dtype  \n",
            "---  ------                        --------------  -----  \n",
            " 0   tweet_id                      14640 non-null  int64  \n",
            " 1   airline_sentiment             14640 non-null  object \n",
            " 2   airline_sentiment_confidence  14640 non-null  float64\n",
            " 3   negativereason                14640 non-null  object \n",
            " 4   negativereason_confidence     10522 non-null  object \n",
            " 5   airline                       14640 non-null  object \n",
            " 6   name                          14640 non-null  object \n",
            " 7   retweet_count                 14640 non-null  int64  \n",
            " 8   text                          14640 non-null  object \n",
            " 9   tweet_created                 14640 non-null  object \n",
            " 10  tweet_location                9907 non-null   object \n",
            " 11  user_timezone                 9820 non-null   object \n",
            "dtypes: float64(1), int64(2), object(9)\n",
            "memory usage: 1.3+ MB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mXMmRLK9SyY_",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a703fd9f-0670-41fd-d010-526b4e40a6f4"
      },
      "source": [
        "dataset.user_timezone.nunique()"
      ],
      "execution_count": 128,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "85"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 128
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lWyUMWiaS8sG",
        "trusted": true
      },
      "source": [
        "#trés bien juste 85 uniques valeurs qui se répétent dans plus de 9000 lignes"
      ],
      "execution_count": 129,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AjADBRAGTEj6",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "51b36be4-fb06-4138-f9de-5e7ccb44d81d"
      },
      "source": [
        "nr = dataset.user_timezone.unique()\n",
        "nr.reshape(1,86)"
      ],
      "execution_count": 130,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([['Eastern Time (US & Canada)', 'Pacific Time (US & Canada)',\n",
              "        'Central Time (US & Canada)', 'America/New_York',\n",
              "        'Atlantic Time (Canada)', 'Quito', nan,\n",
              "        'Mountain Time (US & Canada)', 'Vienna', 'Caracas',\n",
              "        'Kuala Lumpur', 'Brisbane', 'Arizona', 'London', 'Tehran',\n",
              "        'Alaska', 'Sydney', 'Irkutsk', 'Santiago', 'Amsterdam',\n",
              "        'Tijuana', 'Abu Dhabi', 'Central America', 'Edinburgh',\n",
              "        'Jerusalem', 'Hawaii', 'Paris', 'Guam', 'New Delhi', 'Stockholm',\n",
              "        'America/Chicago', 'Berlin', 'Madrid', 'Athens', 'Brussels',\n",
              "        'Taipei', 'Rome', 'Beijing', 'Mexico City', 'Bern', 'Singapore',\n",
              "        'Indiana (East)', 'Melbourne', 'Saskatchewan', 'Casablanca',\n",
              "        'Brasilia', 'Kyiv', 'Bucharest', 'Greenland', 'Prague',\n",
              "        'New Caledonia', 'Bogota', 'Seoul', 'Sarajevo', 'Wellington',\n",
              "        'Bangkok', 'Warsaw', 'Copenhagen', 'Hong Kong', 'Guadalajara',\n",
              "        'Mid-Atlantic', 'Mazatlan', 'Buenos Aires',\n",
              "        'America/Los_Angeles', 'Dublin', 'Lisbon', 'Newfoundland',\n",
              "        'Monterrey', 'Tokyo', 'America/Detroit', 'Midway Island',\n",
              "        'Istanbul', 'Solomon Is.', 'America/Atikokan', 'Adelaide',\n",
              "        'Nairobi', 'EST', 'Lima', 'Islamabad', 'Helsinki', 'Pretoria',\n",
              "        'West Central Africa', 'America/Boise', 'Canberra', 'Perth',\n",
              "        'La Paz']], dtype=object)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 130
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cSWcQfU_TS1G",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2d4c0623-732b-4844-8a54-9995ff3143d5"
      },
      "source": [
        "for k in range (dataset.shape[0]):\n",
        "  if dataset.user_timezone.iloc[k] is np.NaN:\n",
        "    p = random.randint(1, 85)\n",
        "    dataset.user_timezone.iloc[k] = nr[p]"
      ],
      "execution_count": 131,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  iloc._setitem_with_indexer(indexer, value)\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-cM6sbKgTdcG",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "438e9117-a5e0-4103-cebc-6a924f46d805"
      },
      "source": [
        "dataset.info()"
      ],
      "execution_count": 132,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 14640 entries, 0 to 14639\n",
            "Data columns (total 12 columns):\n",
            " #   Column                        Non-Null Count  Dtype  \n",
            "---  ------                        --------------  -----  \n",
            " 0   tweet_id                      14640 non-null  int64  \n",
            " 1   airline_sentiment             14640 non-null  object \n",
            " 2   airline_sentiment_confidence  14640 non-null  float64\n",
            " 3   negativereason                14640 non-null  object \n",
            " 4   negativereason_confidence     10522 non-null  object \n",
            " 5   airline                       14640 non-null  object \n",
            " 6   name                          14640 non-null  object \n",
            " 7   retweet_count                 14640 non-null  int64  \n",
            " 8   text                          14640 non-null  object \n",
            " 9   tweet_created                 14640 non-null  object \n",
            " 10  tweet_location                9907 non-null   object \n",
            " 11  user_timezone                 14582 non-null  object \n",
            "dtypes: float64(1), int64(2), object(9)\n",
            "memory usage: 1.3+ MB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1C395R9GTi0Y",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "20383bf3-bf44-454a-d1ea-fc7d58525ada"
      },
      "source": [
        "dataset.tweet_location.nunique()"
      ],
      "execution_count": 133,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3081"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 133
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5wEO53NPVe-_",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "7f32beee-2885-4539-9698-632f5192d015"
      },
      "source": [
        "nr = dataset.tweet_location.unique()\n",
        "nr.shape"
      ],
      "execution_count": 134,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(3082,)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 134
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rYHdU9RJVk16",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "95e3d868-d53e-4081-f2c8-cac22cbfa872"
      },
      "source": [
        "nr.reshape(1,3082)"
      ],
      "execution_count": 135,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[nan, 'Lets Play', 'San Francisco CA', ..., 'Columbus, OH, USA',\n",
              "        'Milwaukee County, Wisconsin', 'Nigeria,lagos']], dtype=object)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 135
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "o3mQo3uDTz99",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "79b85f8b-96cd-4ba5-b85b-8e11fc41f650"
      },
      "source": [
        "for k in range (dataset.shape[0]):\n",
        "  if dataset.tweet_location.iloc[k] is np.NaN:\n",
        "    p = random.randint(1, 3081)\n",
        "    dataset.tweet_location.iloc[k] = nr[p]"
      ],
      "execution_count": 136,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  iloc._setitem_with_indexer(indexer, value)\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RXjeXgAeVvsV",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f714fcdd-ef27-4620-f547-2a4b8e430c47"
      },
      "source": [
        "dataset.info()"
      ],
      "execution_count": 137,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 14640 entries, 0 to 14639\n",
            "Data columns (total 12 columns):\n",
            " #   Column                        Non-Null Count  Dtype  \n",
            "---  ------                        --------------  -----  \n",
            " 0   tweet_id                      14640 non-null  int64  \n",
            " 1   airline_sentiment             14640 non-null  object \n",
            " 2   airline_sentiment_confidence  14640 non-null  float64\n",
            " 3   negativereason                14640 non-null  object \n",
            " 4   negativereason_confidence     10522 non-null  object \n",
            " 5   airline                       14640 non-null  object \n",
            " 6   name                          14640 non-null  object \n",
            " 7   retweet_count                 14640 non-null  int64  \n",
            " 8   text                          14640 non-null  object \n",
            " 9   tweet_created                 14640 non-null  object \n",
            " 10  tweet_location                14640 non-null  object \n",
            " 11  user_timezone                 14582 non-null  object \n",
            "dtypes: float64(1), int64(2), object(9)\n",
            "memory usage: 1.3+ MB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yOhSS5tjVzpC",
        "trusted": true
      },
      "source": [
        "#ilya un probléme avec la colonne 'negativereason_confidence'"
      ],
      "execution_count": 138,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HNCcOXUeWdFD",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 452
        },
        "outputId": "b61be2ba-67d1-4887-9c5d-1b0e29b7f2cf"
      },
      "source": [
        "dataset.head()"
      ],
      "execution_count": 139,
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
              "      <th>tweet_id</th>\n",
              "      <th>airline_sentiment</th>\n",
              "      <th>airline_sentiment_confidence</th>\n",
              "      <th>negativereason</th>\n",
              "      <th>negativereason_confidence</th>\n",
              "      <th>airline</th>\n",
              "      <th>name</th>\n",
              "      <th>retweet_count</th>\n",
              "      <th>text</th>\n",
              "      <th>tweet_created</th>\n",
              "      <th>tweet_location</th>\n",
              "      <th>user_timezone</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>570306133677760513</td>\n",
              "      <td>neutral</td>\n",
              "      <td>1.0000</td>\n",
              "      <td>Bad Flight</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Virgin America</td>\n",
              "      <td>cairdin</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica What @dhepburn said.</td>\n",
              "      <td>2015-02-24 11:35:52 -0800</td>\n",
              "      <td>Lawrence, MA</td>\n",
              "      <td>Eastern Time (US &amp; Canada)</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>570301130888122368</td>\n",
              "      <td>positive</td>\n",
              "      <td>0.3486</td>\n",
              "      <td>Late Flight</td>\n",
              "      <td>0</td>\n",
              "      <td>Virgin America</td>\n",
              "      <td>jnardino</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica plus you've added commercials t...</td>\n",
              "      <td>2015-02-24 11:15:59 -0800</td>\n",
              "      <td>The happiest place on Earth!</td>\n",
              "      <td>Pacific Time (US &amp; Canada)</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>570301083672813571</td>\n",
              "      <td>neutral</td>\n",
              "      <td>0.6837</td>\n",
              "      <td>Bad Flight</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Virgin America</td>\n",
              "      <td>yvonnalynn</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica I didn't today... Must mean I n...</td>\n",
              "      <td>2015-02-24 11:15:48 -0800</td>\n",
              "      <td>Lets Play</td>\n",
              "      <td>Central Time (US &amp; Canada)</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>570301031407624196</td>\n",
              "      <td>negative</td>\n",
              "      <td>1.0000</td>\n",
              "      <td>Bad Flight</td>\n",
              "      <td>0.7033</td>\n",
              "      <td>Virgin America</td>\n",
              "      <td>jnardino</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica it's really aggressive to blast...</td>\n",
              "      <td>2015-02-24 11:15:36 -0800</td>\n",
              "      <td>los angeles ca</td>\n",
              "      <td>Pacific Time (US &amp; Canada)</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>570300817074462722</td>\n",
              "      <td>negative</td>\n",
              "      <td>1.0000</td>\n",
              "      <td>Can't Tell</td>\n",
              "      <td>1</td>\n",
              "      <td>Virgin America</td>\n",
              "      <td>jnardino</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica and it's a really big bad thing...</td>\n",
              "      <td>2015-02-24 11:14:45 -0800</td>\n",
              "      <td>Always around</td>\n",
              "      <td>Pacific Time (US &amp; Canada)</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "             tweet_id  ...               user_timezone\n",
              "0  570306133677760513  ...  Eastern Time (US & Canada)\n",
              "1  570301130888122368  ...  Pacific Time (US & Canada)\n",
              "2  570301083672813571  ...  Central Time (US & Canada)\n",
              "3  570301031407624196  ...  Pacific Time (US & Canada)\n",
              "4  570300817074462722  ...  Pacific Time (US & Canada)\n",
              "\n",
              "[5 rows x 12 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 139
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9LiUvaWoWnOA",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6dc02201-b73e-42dd-99c3-b4e30ba2e679"
      },
      "source": [
        "dataset.negativereason_confidence.iloc[0]  in range(0,2)"
      ],
      "execution_count": 140,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 140
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nthpG3cTXWVM",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3da44baa-2cb3-42df-e84a-19c4d879547e"
      },
      "source": [
        "dataset.negativereason_confidence.iloc[0] = 1"
      ],
      "execution_count": 141,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  iloc._setitem_with_indexer(indexer, value)\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Sre7UMcmXUVk",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b8ac8880-fdd8-4101-a3ef-476951d3cc91"
      },
      "source": [
        "dataset.negativereason_confidence.iloc[0]  "
      ],
      "execution_count": 142,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 142
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "us7edCqZXcy9",
        "trusted": true
      },
      "source": [
        "nr = dataset.negativereason_confidence.unique()"
      ],
      "execution_count": 143,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nGdZwKubXhLe",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "9b3d84ff-b843-4a65-9985-237b83c6bf9b"
      },
      "source": [
        "nr.shape"
      ],
      "execution_count": 144,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(1411,)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 144
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0Inhh0l1XjM1",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "824cb0d9-94e1-402f-950c-15dfcbf162d2"
      },
      "source": [
        "nr.reshape(1,1411)"
      ],
      "execution_count": 145,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[1, 0.0, nan, ..., 0.6234, 0.644, 0.7255]], dtype=object)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 145
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HDiOH9H6XjLl",
        "trusted": true
      },
      "source": [
        "nr[2] = 0.644"
      ],
      "execution_count": 146,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ATu1nwV6YCy_",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "9c7bb554-850b-47d4-acba-69e7a725afdb"
      },
      "source": [
        "nr"
      ],
      "execution_count": 147,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([1, 0.0, 0.644, ..., 0.6234, 0.644, 0.7255], dtype=object)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 147
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "F3Nb7tTzWsu5",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0366126c-21d8-4d53-8ba8-27c664d683fa"
      },
      "source": [
        "for k in range (dataset.shape[0]):\n",
        "  if dataset.negativereason_confidence.iloc[k] not in range(0,2):\n",
        "    p = random.randint(0,1410)\n",
        "    dataset.negativereason_confidence.iloc[k] = nr[p]"
      ],
      "execution_count": 148,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  iloc._setitem_with_indexer(indexer, value)\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IwPLhhnXYXrC",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f8ebe16f-85dd-49e9-e23f-248f2137ce5a"
      },
      "source": [
        "dataset.info()"
      ],
      "execution_count": 149,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 14640 entries, 0 to 14639\n",
            "Data columns (total 12 columns):\n",
            " #   Column                        Non-Null Count  Dtype  \n",
            "---  ------                        --------------  -----  \n",
            " 0   tweet_id                      14640 non-null  int64  \n",
            " 1   airline_sentiment             14640 non-null  object \n",
            " 2   airline_sentiment_confidence  14640 non-null  float64\n",
            " 3   negativereason                14640 non-null  object \n",
            " 4   negativereason_confidence     14640 non-null  object \n",
            " 5   airline                       14640 non-null  object \n",
            " 6   name                          14640 non-null  object \n",
            " 7   retweet_count                 14640 non-null  int64  \n",
            " 8   text                          14640 non-null  object \n",
            " 9   tweet_created                 14640 non-null  object \n",
            " 10  tweet_location                14640 non-null  object \n",
            " 11  user_timezone                 14582 non-null  object \n",
            "dtypes: float64(1), int64(2), object(9)\n",
            "memory usage: 1.3+ MB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "w2u42rgwYhBo",
        "trusted": true
      },
      "source": [
        "#trés bien "
      ],
      "execution_count": 150,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "p7tXPapxonKO",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 452
        },
        "outputId": "918df8ce-2c31-4018-ba56-0b642e876c27"
      },
      "source": [
        "dataset.head()"
      ],
      "execution_count": 151,
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
              "      <th>tweet_id</th>\n",
              "      <th>airline_sentiment</th>\n",
              "      <th>airline_sentiment_confidence</th>\n",
              "      <th>negativereason</th>\n",
              "      <th>negativereason_confidence</th>\n",
              "      <th>airline</th>\n",
              "      <th>name</th>\n",
              "      <th>retweet_count</th>\n",
              "      <th>text</th>\n",
              "      <th>tweet_created</th>\n",
              "      <th>tweet_location</th>\n",
              "      <th>user_timezone</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>570306133677760513</td>\n",
              "      <td>neutral</td>\n",
              "      <td>1.0000</td>\n",
              "      <td>Bad Flight</td>\n",
              "      <td>1</td>\n",
              "      <td>Virgin America</td>\n",
              "      <td>cairdin</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica What @dhepburn said.</td>\n",
              "      <td>2015-02-24 11:35:52 -0800</td>\n",
              "      <td>Lawrence, MA</td>\n",
              "      <td>Eastern Time (US &amp; Canada)</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>570301130888122368</td>\n",
              "      <td>positive</td>\n",
              "      <td>0.3486</td>\n",
              "      <td>Late Flight</td>\n",
              "      <td>0</td>\n",
              "      <td>Virgin America</td>\n",
              "      <td>jnardino</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica plus you've added commercials t...</td>\n",
              "      <td>2015-02-24 11:15:59 -0800</td>\n",
              "      <td>The happiest place on Earth!</td>\n",
              "      <td>Pacific Time (US &amp; Canada)</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>570301083672813571</td>\n",
              "      <td>neutral</td>\n",
              "      <td>0.6837</td>\n",
              "      <td>Bad Flight</td>\n",
              "      <td>0.6342</td>\n",
              "      <td>Virgin America</td>\n",
              "      <td>yvonnalynn</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica I didn't today... Must mean I n...</td>\n",
              "      <td>2015-02-24 11:15:48 -0800</td>\n",
              "      <td>Lets Play</td>\n",
              "      <td>Central Time (US &amp; Canada)</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>570301031407624196</td>\n",
              "      <td>negative</td>\n",
              "      <td>1.0000</td>\n",
              "      <td>Bad Flight</td>\n",
              "      <td>0.6803</td>\n",
              "      <td>Virgin America</td>\n",
              "      <td>jnardino</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica it's really aggressive to blast...</td>\n",
              "      <td>2015-02-24 11:15:36 -0800</td>\n",
              "      <td>los angeles ca</td>\n",
              "      <td>Pacific Time (US &amp; Canada)</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>570300817074462722</td>\n",
              "      <td>negative</td>\n",
              "      <td>1.0000</td>\n",
              "      <td>Can't Tell</td>\n",
              "      <td>1</td>\n",
              "      <td>Virgin America</td>\n",
              "      <td>jnardino</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica and it's a really big bad thing...</td>\n",
              "      <td>2015-02-24 11:14:45 -0800</td>\n",
              "      <td>Always around</td>\n",
              "      <td>Pacific Time (US &amp; Canada)</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "             tweet_id  ...               user_timezone\n",
              "0  570306133677760513  ...  Eastern Time (US & Canada)\n",
              "1  570301130888122368  ...  Pacific Time (US & Canada)\n",
              "2  570301083672813571  ...  Central Time (US & Canada)\n",
              "3  570301031407624196  ...  Pacific Time (US & Canada)\n",
              "4  570300817074462722  ...  Pacific Time (US & Canada)\n",
              "\n",
              "[5 rows x 12 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 151
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mEQj5t__optg",
        "trusted": true
      },
      "source": [
        "dataset.drop(['tweet_id'],axis=1,inplace=True)"
      ],
      "execution_count": 152,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JP0AsOhXoxjp",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "038ce2e3-7f8f-4e70-a412-551ff5be6780"
      },
      "source": [
        "dataset.name.nunique()"
      ],
      "execution_count": 153,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "7701"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 153
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SlkZKDFEo89Z",
        "trusted": true
      },
      "source": [
        "X = dataset.drop(['airline_sentiment'],axis=1)\n",
        "y = dataset.airline_sentiment"
      ],
      "execution_count": 154,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9pso9DIbpVF6",
        "trusted": true
      },
      "source": [
        "y = y.replace({'negative' : 0 , 'neutral' : 1 , 'positive' : 2})"
      ],
      "execution_count": 155,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "p2AIEGzjpp0i",
        "trusted": true
      },
      "source": [
        "#on va traiter la colonne \"tweet_created\""
      ],
      "execution_count": 156,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eOHwsyfsqEJJ",
        "trusted": true
      },
      "source": [
        "X['year'] = pd.to_datetime(X.tweet_created).dt.year\n",
        "X['day'] = pd.to_datetime(X.tweet_created).dt.day\n",
        "X['month'] = pd.to_datetime(X.tweet_created).dt.month\n",
        "X['hour'] = pd.to_datetime(X.tweet_created).dt.hour\n",
        "X['minute'] = pd.to_datetime(X.tweet_created).dt.minute\n",
        "X['second'] = pd.to_datetime(X.tweet_created).dt.second"
      ],
      "execution_count": 157,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GYJ25kZFrE86",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 452
        },
        "outputId": "9a68289b-2d69-4daa-d3d2-1b5fa76cc513"
      },
      "source": [
        "X.head()"
      ],
      "execution_count": 158,
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
              "      <th>airline_sentiment_confidence</th>\n",
              "      <th>negativereason</th>\n",
              "      <th>negativereason_confidence</th>\n",
              "      <th>airline</th>\n",
              "      <th>name</th>\n",
              "      <th>retweet_count</th>\n",
              "      <th>text</th>\n",
              "      <th>tweet_created</th>\n",
              "      <th>tweet_location</th>\n",
              "      <th>user_timezone</th>\n",
              "      <th>year</th>\n",
              "      <th>day</th>\n",
              "      <th>month</th>\n",
              "      <th>hour</th>\n",
              "      <th>minute</th>\n",
              "      <th>second</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1.0000</td>\n",
              "      <td>Bad Flight</td>\n",
              "      <td>1</td>\n",
              "      <td>Virgin America</td>\n",
              "      <td>cairdin</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica What @dhepburn said.</td>\n",
              "      <td>2015-02-24 11:35:52 -0800</td>\n",
              "      <td>Lawrence, MA</td>\n",
              "      <td>Eastern Time (US &amp; Canada)</td>\n",
              "      <td>2015</td>\n",
              "      <td>24</td>\n",
              "      <td>2</td>\n",
              "      <td>11</td>\n",
              "      <td>35</td>\n",
              "      <td>52</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0.3486</td>\n",
              "      <td>Late Flight</td>\n",
              "      <td>0</td>\n",
              "      <td>Virgin America</td>\n",
              "      <td>jnardino</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica plus you've added commercials t...</td>\n",
              "      <td>2015-02-24 11:15:59 -0800</td>\n",
              "      <td>The happiest place on Earth!</td>\n",
              "      <td>Pacific Time (US &amp; Canada)</td>\n",
              "      <td>2015</td>\n",
              "      <td>24</td>\n",
              "      <td>2</td>\n",
              "      <td>11</td>\n",
              "      <td>15</td>\n",
              "      <td>59</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0.6837</td>\n",
              "      <td>Bad Flight</td>\n",
              "      <td>0.6342</td>\n",
              "      <td>Virgin America</td>\n",
              "      <td>yvonnalynn</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica I didn't today... Must mean I n...</td>\n",
              "      <td>2015-02-24 11:15:48 -0800</td>\n",
              "      <td>Lets Play</td>\n",
              "      <td>Central Time (US &amp; Canada)</td>\n",
              "      <td>2015</td>\n",
              "      <td>24</td>\n",
              "      <td>2</td>\n",
              "      <td>11</td>\n",
              "      <td>15</td>\n",
              "      <td>48</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1.0000</td>\n",
              "      <td>Bad Flight</td>\n",
              "      <td>0.6803</td>\n",
              "      <td>Virgin America</td>\n",
              "      <td>jnardino</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica it's really aggressive to blast...</td>\n",
              "      <td>2015-02-24 11:15:36 -0800</td>\n",
              "      <td>los angeles ca</td>\n",
              "      <td>Pacific Time (US &amp; Canada)</td>\n",
              "      <td>2015</td>\n",
              "      <td>24</td>\n",
              "      <td>2</td>\n",
              "      <td>11</td>\n",
              "      <td>15</td>\n",
              "      <td>36</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1.0000</td>\n",
              "      <td>Can't Tell</td>\n",
              "      <td>1</td>\n",
              "      <td>Virgin America</td>\n",
              "      <td>jnardino</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica and it's a really big bad thing...</td>\n",
              "      <td>2015-02-24 11:14:45 -0800</td>\n",
              "      <td>Always around</td>\n",
              "      <td>Pacific Time (US &amp; Canada)</td>\n",
              "      <td>2015</td>\n",
              "      <td>24</td>\n",
              "      <td>2</td>\n",
              "      <td>11</td>\n",
              "      <td>14</td>\n",
              "      <td>45</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   airline_sentiment_confidence negativereason  ... minute second\n",
              "0                        1.0000     Bad Flight  ...     35     52\n",
              "1                        0.3486    Late Flight  ...     15     59\n",
              "2                        0.6837     Bad Flight  ...     15     48\n",
              "3                        1.0000     Bad Flight  ...     15     36\n",
              "4                        1.0000     Can't Tell  ...     14     45\n",
              "\n",
              "[5 rows x 16 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 158
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Li5Ttj2jrHG4",
        "trusted": true
      },
      "source": [
        "X.drop(['tweet_created'],axis=1,inplace=True)"
      ],
      "execution_count": 159,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BJ8YuedusAET",
        "trusted": true
      },
      "source": [
        "X.drop(['name'],axis=1,inplace=True)"
      ],
      "execution_count": 160,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Hva3fIi1rQKX",
        "trusted": true
      },
      "source": [
        "from sklearn.preprocessing import LabelEncoder"
      ],
      "execution_count": 161,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "thN5iSM0r4z9",
        "trusted": true
      },
      "source": [
        "X.negativereason = X.negativereason.astype('str')\n",
        "X.airline = X.airline.astype('str')\n",
        "X.tweet_location = X.tweet_location.astype('str')\n",
        "X.user_timezone = X.user_timezone.astype('str')\n",
        "columns_to_Encode = [\"negativereason\",\"airline\",\"tweet_location\",\"user_timezone\"]\n",
        "le = LabelEncoder()\n",
        "for each in columns_to_Encode:\n",
        "    X[each] = le.fit_transform(X[each])"
      ],
      "execution_count": 162,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "N8ZUhuEcsfsu",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 452
        },
        "outputId": "5eb268ab-d510-4674-ad8e-09bc79df9ffd"
      },
      "source": [
        "X.head()"
      ],
      "execution_count": 163,
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
              "      <th>airline_sentiment_confidence</th>\n",
              "      <th>negativereason</th>\n",
              "      <th>negativereason_confidence</th>\n",
              "      <th>airline</th>\n",
              "      <th>retweet_count</th>\n",
              "      <th>text</th>\n",
              "      <th>tweet_location</th>\n",
              "      <th>user_timezone</th>\n",
              "      <th>year</th>\n",
              "      <th>day</th>\n",
              "      <th>month</th>\n",
              "      <th>hour</th>\n",
              "      <th>minute</th>\n",
              "      <th>second</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1.0000</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>5</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica What @dhepburn said.</td>\n",
              "      <td>1206</td>\n",
              "      <td>31</td>\n",
              "      <td>2015</td>\n",
              "      <td>24</td>\n",
              "      <td>2</td>\n",
              "      <td>11</td>\n",
              "      <td>35</td>\n",
              "      <td>52</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0.3486</td>\n",
              "      <td>7</td>\n",
              "      <td>0</td>\n",
              "      <td>5</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica plus you've added commercials t...</td>\n",
              "      <td>2375</td>\n",
              "      <td>62</td>\n",
              "      <td>2015</td>\n",
              "      <td>24</td>\n",
              "      <td>2</td>\n",
              "      <td>11</td>\n",
              "      <td>15</td>\n",
              "      <td>59</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0.6837</td>\n",
              "      <td>0</td>\n",
              "      <td>0.6342</td>\n",
              "      <td>5</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica I didn't today... Must mean I n...</td>\n",
              "      <td>1219</td>\n",
              "      <td>27</td>\n",
              "      <td>2015</td>\n",
              "      <td>24</td>\n",
              "      <td>2</td>\n",
              "      <td>11</td>\n",
              "      <td>15</td>\n",
              "      <td>48</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1.0000</td>\n",
              "      <td>0</td>\n",
              "      <td>0.6803</td>\n",
              "      <td>5</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica it's really aggressive to blast...</td>\n",
              "      <td>2816</td>\n",
              "      <td>62</td>\n",
              "      <td>2015</td>\n",
              "      <td>24</td>\n",
              "      <td>2</td>\n",
              "      <td>11</td>\n",
              "      <td>15</td>\n",
              "      <td>36</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1.0000</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>5</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica and it's a really big bad thing...</td>\n",
              "      <td>150</td>\n",
              "      <td>62</td>\n",
              "      <td>2015</td>\n",
              "      <td>24</td>\n",
              "      <td>2</td>\n",
              "      <td>11</td>\n",
              "      <td>14</td>\n",
              "      <td>45</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   airline_sentiment_confidence  negativereason  ... minute  second\n",
              "0                        1.0000               0  ...     35      52\n",
              "1                        0.3486               7  ...     15      59\n",
              "2                        0.6837               0  ...     15      48\n",
              "3                        1.0000               0  ...     15      36\n",
              "4                        1.0000               1  ...     14      45\n",
              "\n",
              "[5 rows x 14 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 163
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kCaZIlO2tzzI",
        "trusted": true
      },
      "source": [
        "#Etape suivante : traiter la colonne \"text\""
      ],
      "execution_count": 164,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Vzssx5RSt81T",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 486
        },
        "outputId": "f241ca09-99c4-432a-a3e7-1daa987692e2"
      },
      "source": [
        "X.tail()"
      ],
      "execution_count": 165,
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
              "      <th>airline_sentiment_confidence</th>\n",
              "      <th>negativereason</th>\n",
              "      <th>negativereason_confidence</th>\n",
              "      <th>airline</th>\n",
              "      <th>retweet_count</th>\n",
              "      <th>text</th>\n",
              "      <th>tweet_location</th>\n",
              "      <th>user_timezone</th>\n",
              "      <th>year</th>\n",
              "      <th>day</th>\n",
              "      <th>month</th>\n",
              "      <th>hour</th>\n",
              "      <th>minute</th>\n",
              "      <th>second</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>14635</th>\n",
              "      <td>0.3487</td>\n",
              "      <td>8</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>@AmericanAir thank you we got on a different f...</td>\n",
              "      <td>1239</td>\n",
              "      <td>35</td>\n",
              "      <td>2015</td>\n",
              "      <td>22</td>\n",
              "      <td>2</td>\n",
              "      <td>12</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14636</th>\n",
              "      <td>1.0000</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>@AmericanAir leaving over 20 minutes Late Flig...</td>\n",
              "      <td>2324</td>\n",
              "      <td>83</td>\n",
              "      <td>2015</td>\n",
              "      <td>22</td>\n",
              "      <td>2</td>\n",
              "      <td>11</td>\n",
              "      <td>59</td>\n",
              "      <td>46</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14637</th>\n",
              "      <td>1.0000</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>@AmericanAir Please bring American Airlines to...</td>\n",
              "      <td>1670</td>\n",
              "      <td>37</td>\n",
              "      <td>2015</td>\n",
              "      <td>22</td>\n",
              "      <td>2</td>\n",
              "      <td>11</td>\n",
              "      <td>59</td>\n",
              "      <td>15</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14638</th>\n",
              "      <td>1.0000</td>\n",
              "      <td>3</td>\n",
              "      <td>0.3575</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>@AmericanAir you have my money, you change my ...</td>\n",
              "      <td>1599</td>\n",
              "      <td>31</td>\n",
              "      <td>2015</td>\n",
              "      <td>22</td>\n",
              "      <td>2</td>\n",
              "      <td>11</td>\n",
              "      <td>59</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14639</th>\n",
              "      <td>0.6771</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>@AmericanAir we have 8 ppl so we need 2 know h...</td>\n",
              "      <td>2719</td>\n",
              "      <td>5</td>\n",
              "      <td>2015</td>\n",
              "      <td>22</td>\n",
              "      <td>2</td>\n",
              "      <td>11</td>\n",
              "      <td>58</td>\n",
              "      <td>51</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "       airline_sentiment_confidence  negativereason  ... minute  second\n",
              "14635                        0.3487               8  ...      1       1\n",
              "14636                        1.0000               3  ...     59      46\n",
              "14637                        1.0000               3  ...     59      15\n",
              "14638                        1.0000               3  ...     59       2\n",
              "14639                        0.6771               6  ...     58      51\n",
              "\n",
              "[5 rows x 14 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 165
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xb11exNqvfry",
        "trusted": true
      },
      "source": [
        "X['len_text'] = X['text'].apply(len)"
      ],
      "execution_count": 166,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tDee1Hhswtho",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 427
        },
        "outputId": "7fab1de4-9b0f-41e7-9b7e-015dd771bc33"
      },
      "source": [
        "plt.style.use('seaborn-darkgrid')\n",
        "plt.figure(figsize=(10,5))\n",
        "sns.distplot(X['len_text'],kde=False,color='red',hist=True)\n",
        "plt.xlabel(\"text Length\",size=15)\n",
        "plt.ylabel(\"Frequency\",size=15)\n",
        "plt.title(\"Length Histogram\",size=15)"
      ],
      "execution_count": 167,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/seaborn/distributions.py:2557: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).\n",
            "  warnings.warn(msg, FutureWarning)\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Text(0.5, 1.0, 'Length Histogram')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 167
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAmgAAAFOCAYAAAAy8uH/AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nO3de1xU9b7/8fdwGQYCQxTspuXxfrwb5d0UJS+VWQmpoelG0+PdKFS6aMeM1Nx6vJTJNtO0NOlGpaKV3XZIGm2D+hWRe5eZ6aCYKCoI8/uj45zYYIM4zFo4r+fj4ePRrFmXz3xcTe++37XWWBwOh0MAAAAwDR+jCwAAAEB5BDQAAACTIaABAACYDAENAADAZAhoAAAAJkNAAwAAMBkCGoDLSmZmplq0aKFff/21Rvbfv39/rVixokb2DQDnEdAAVNvIkSP10EMPGV2GnnvuOZWVlVV7++XLl6tXr16VvrdkyRJFRUU5X6enp2vy5MlV2u/evXuVkZFR7boAeC8CGoBa7bvvvtPSpUsvKaDVlHXr1mn37t1GlwGgFiKgAahRGzdu1B133KEOHTqoV69eWrRokc6dOyfp/6Yj//GPfyg2NlYdOnRQ//799dFHHzm3//HHHxUXF6d27dopOjpa27dv12233ably5fro48+0t133y1J6tixo9asWePcbv/+/Ro2bJjatWun3r1764MPPnDL54mKitKSJUskSQUFBUpISFC3bt3UoUMHDRgwQK+++qokadiwYdqxY4dSUlIUGRkpSTp37pyeffZZDRgwQO3atVOfPn20YsWKcuFy9erV6t69uzp27Khp06Zpy5YtatGihfP9Fi1a6MUXX1T//v01evRo52d94IEH1KVLF914442677779PXXXzu3GTlypBYsWKD58+crMjJS3bp105YtW7R3714NHjxYHTp0UFxcnA4fPuyWHgG4dAQ0ADUmNTVVy5Yt05w5c5SVlaXVq1dr69atWrVqVbn1li9frsWLF+vzzz9Xx44dNWvWLJ3/FbpHH31UJSUl+uCDD7R582a99tprOnTokCTplltu0bx58yRJX375peLj4537XL9+vZ555hnt2bNHN998sx555BG3j7ItWbJEBQUF2r59u7KysvTYY48pOTlZeXl52rRpk6699lqNGzdOe/fulfT7VOym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s8qdO/7+/kpISFB8fLwsFosmTZqkkBDv+Fmaynp09OhRBQQEaOTIkZJ+/83kuXPn6qqrrtLQoUPl4+OjqKgor7nou7IexcXFVfiettlsnEd/6NHy5ctlt9udI/mSFBkZqTfffFP33nuvSktL9cADD6hBgwYGVu4ZFgcT3gAAAKbCFCcAAIDJENAAAABMhoAGAABgMgQ0AAAAkyGgAQAAmAwBDQBMauTIkXrkkUeMLgOAAQhoAExn7969bv0x+9zcXO3YseOC72dmZqpFixb68ccf3XbM6nD35wZQexHQAJjOunXrtHv3brft7/XXX//TgGYW7v7cAGovfkkAgKkMGzZMX375pXx9fbVx40bt3btXpaWleu655/T222/r119/Vf369TV8+HCNHTtWDodDf/nLX2S1WvX8889LkgoKCjRo0CCNGzdOX3/9td59911ZLBalp6dr165dql+//kXX9fPPP+vpp5/Wl19+qVOnTql169ZKTExU+/btJf0+HdmmTRtZrVZt2bJFxcXF6tWrl5566inZbDZJ0urVq7Vu3ToVFRWpV69e6tGjhx599FF99913lX7u81asWKFXXnlFhYWF6t27t5KTk3XFFVe4odsAzIoRNACmsmnTJl177bUaN26cM6SsWLFCb775ppYtW6asrCwtWLBAzz33nN58801ZLBYlJycrKytLW7dulSQtWLBATZs21ZgxY7R48WLddNNNuu2225SdnV2tcFZcXKwxY8YoNDRU27dvV0ZGhm688UaNHTtWJ0+edK73xhtv6Oqrr9aHH36oDRs2aOfOnUpNTZX0+zTq4sWLNXPmTGVmZmrQoEFaunTpn35uSfroo48UERGhXbt2adOmTfrggw/0+uuvV6u3AGoPAhoAUysrK9PLL7+scePGqUWLFvL19VVkZKRiYmL06quvSpKuuuoqPf7443rqqaeUnp6u9957TwsWLJDFYnFLDR9//LF++eUXJSUlKSQkRIGBgZoxY4Z8fX21bds253rXXXedhg0bJqvVqpYtW6pFixb67rvvJEnbtm1TixYtNHjwYFmtVvXv319dunRxeexrrrlGsbGxslqt+s///E81b95c33//vVs+FwDzYooTgKkdO3ZMx48f17x58/Tkk086lzscDoWHhztf33HHHdq5c6emTZum+fPn65prrnFbDfv379e5c+fUuXPncsvLysp08OBB5+vrr7++3PuBgYE6ffq0JOnXX38t9wPQktShQwe98847f3rshg0blnsdEBCg4uLii/4MAGoXAhoAUzt//daSJUsUHR19wfXOnTungwcPKigoSD/88IPbawgODtYXX3zxp+v92YhdWVmZ/P39q7z+xawD4PLDFCcAUwsODlb9+vX1zTfflFt++PDhciNJq1atUnFxsV5++WVt3LhRe/bscVsNN9xwg06ePKmffvqp3PIDBw5UeR/h4eEV1v/yyy/dUh+Ayw8BDYDpBAYG6qefflJhYaFKS0t1//33a+PGjcrIyFBpaam+/fZbjRgxQmvWrJEkff3111q9erXmz5+vli1basKECZo5c6bzAv7AwEAdPHhQhYWF1Zoe7N69u5o2baq5c+c6g+Err7yiQYMGVTmk9evXT9nZ2dq5c6dKSkq0Y8eOCiHy3z83AO9FQANgOiNGjNCHH36ovn37qqCgQPHx8brvvvs0e/ZsdejQQZMmTdJdd92l8ePHq7i4WDNnztR9992ndu3aSZLGjRunOnXqaP78+ZKk2NhY5eXl6ZZbblFubu4Fj3vbbbepbdu25f5s27ZNvr6+WrVqlQICAjRw4EB17dpVb731llavXl3hGrEL6d27t+Lj45WUlKRu3bpp165dio+PLzeF+e+fG4D3sjgcDofRRQCANzh79qwCAgKcr5cvX67XX39du3btMrAqAGbECBoAeMBXX32l9u3ba9u2bSorK1NeXp5ee+019e3b1+jSAJgQI2gA4CGvvvqq1qxZo19//VV169ZVv379NGPGDH4VAEAFBDQAAACTYYoTAADAZAhoAAAAJkNAAwAAMBkCGgAAgMkQ0AAAAEyGgAYAAGAy/x8qaBdYAK6/BwAAAABJRU5ErkJggg==\n",
            "text/plain": [
              "<Figure size 720x360 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UOv2vu4Qw_Va",
        "trusted": true
      },
      "source": [
        "from nltk.stem.porter import PorterStemmer"
      ],
      "execution_count": 168,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bNCcjPQ9xF9B",
        "trusted": true
      },
      "source": [
        "ps = PorterStemmer() #pour \"text preprocessing\"\n",
        "\n",
        "message = []\n",
        "\n",
        "for i in range(0, X.shape[0]):\n",
        "    #accepter que les mots alphabétiques\n",
        "    review = re.sub('[^a-zA-Z]', ' ', X['text'][i])\n",
        "    #convertir tous minuscule\n",
        "    review = review.lower()\n",
        "    #splitter chaque ligne\n",
        "    review = review.split()\n",
        "    #\n",
        "    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]\n",
        "    #construire de nouveau la ligne\n",
        "    review = ' '.join(review)\n",
        "    message.append(review)"
      ],
      "execution_count": 169,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CU08XXJPxToo",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 656
        },
        "outputId": "95c7d3e7-51f1-4be7-e0ee-9683b8cd204f"
      },
      "source": [
        "X['clean_text']=np.empty((len(message),1))\n",
        "for i in range(len(message)):\n",
        "    X['clean_text'][i]=message[i]\n",
        "X['clean_text_len']=X['clean_text'].apply(len)\n",
        "X.head()"
      ],
      "execution_count": 170,
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
              "      <th>airline_sentiment_confidence</th>\n",
              "      <th>negativereason</th>\n",
              "      <th>negativereason_confidence</th>\n",
              "      <th>airline</th>\n",
              "      <th>retweet_count</th>\n",
              "      <th>text</th>\n",
              "      <th>tweet_location</th>\n",
              "      <th>user_timezone</th>\n",
              "      <th>year</th>\n",
              "      <th>day</th>\n",
              "      <th>month</th>\n",
              "      <th>hour</th>\n",
              "      <th>minute</th>\n",
              "      <th>second</th>\n",
              "      <th>len_text</th>\n",
              "      <th>clean_text</th>\n",
              "      <th>clean_text_len</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1.0000</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>5</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica What @dhepburn said.</td>\n",
              "      <td>1206</td>\n",
              "      <td>31</td>\n",
              "      <td>2015</td>\n",
              "      <td>24</td>\n",
              "      <td>2</td>\n",
              "      <td>11</td>\n",
              "      <td>35</td>\n",
              "      <td>52</td>\n",
              "      <td>35</td>\n",
              "      <td>virginamerica dhepburn said</td>\n",
              "      <td>27</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0.3486</td>\n",
              "      <td>7</td>\n",
              "      <td>0</td>\n",
              "      <td>5</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica plus you've added commercials t...</td>\n",
              "      <td>2375</td>\n",
              "      <td>62</td>\n",
              "      <td>2015</td>\n",
              "      <td>24</td>\n",
              "      <td>2</td>\n",
              "      <td>11</td>\n",
              "      <td>15</td>\n",
              "      <td>59</td>\n",
              "      <td>72</td>\n",
              "      <td>virginamerica plu ad commerci experi tacki</td>\n",
              "      <td>42</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0.6837</td>\n",
              "      <td>0</td>\n",
              "      <td>0.6342</td>\n",
              "      <td>5</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica I didn't today... Must mean I n...</td>\n",
              "      <td>1219</td>\n",
              "      <td>27</td>\n",
              "      <td>2015</td>\n",
              "      <td>24</td>\n",
              "      <td>2</td>\n",
              "      <td>11</td>\n",
              "      <td>15</td>\n",
              "      <td>48</td>\n",
              "      <td>71</td>\n",
              "      <td>virginamerica today must mean need take anoth ...</td>\n",
              "      <td>50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1.0000</td>\n",
              "      <td>0</td>\n",
              "      <td>0.6803</td>\n",
              "      <td>5</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica it's really aggressive to blast...</td>\n",
              "      <td>2816</td>\n",
              "      <td>62</td>\n",
              "      <td>2015</td>\n",
              "      <td>24</td>\n",
              "      <td>2</td>\n",
              "      <td>11</td>\n",
              "      <td>15</td>\n",
              "      <td>36</td>\n",
              "      <td>126</td>\n",
              "      <td>virginamerica realli aggress blast obnoxi ente...</td>\n",
              "      <td>80</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1.0000</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>5</td>\n",
              "      <td>0</td>\n",
              "      <td>@VirginAmerica and it's a really big bad thing...</td>\n",
              "      <td>150</td>\n",
              "      <td>62</td>\n",
              "      <td>2015</td>\n",
              "      <td>24</td>\n",
              "      <td>2</td>\n",
              "      <td>11</td>\n",
              "      <td>14</td>\n",
              "      <td>45</td>\n",
              "      <td>55</td>\n",
              "      <td>virginamerica realli big bad thing</td>\n",
              "      <td>34</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   airline_sentiment_confidence  ...  clean_text_len\n",
              "0                        1.0000  ...              27\n",
              "1                        0.3486  ...              42\n",
              "2                        0.6837  ...              50\n",
              "3                        1.0000  ...              80\n",
              "4                        1.0000  ...              34\n",
              "\n",
              "[5 rows x 17 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 170
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hH2-GTQRxiiz",
        "trusted": true
      },
      "source": [
        "from sklearn.feature_extraction.text import CountVectorizer\n",
        "cv = CountVectorizer(max_features=15000)\n",
        "X1 = cv.fit_transform(message).toarray()"
      ],
      "execution_count": 171,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QMC0CZUvyC7a",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "06d72859-68d0-4d09-d5ff-01826b01898d"
      },
      "source": [
        "X1.shape"
      ],
      "execution_count": 172,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(14640, 10805)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 172
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QCWYQDAayYLq",
        "trusted": true
      },
      "source": [
        "X2 = X.copy()"
      ],
      "execution_count": 173,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KLW8u4k2yoXp",
        "trusted": true
      },
      "source": [
        "X2.drop(['text','clean_text'],axis=1,inplace=True)"
      ],
      "execution_count": 174,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EbIe-FYwzCAn",
        "trusted": true
      },
      "source": [
        "X3 = pd.DataFrame(data=X1)"
      ],
      "execution_count": 175,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aWWN2GVv0aWN",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "db6c4419-a292-4413-e50d-7f00cb34c855"
      },
      "source": [
        "X3.shape"
      ],
      "execution_count": 176,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(14640, 10805)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 176
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_cbXdNF_0cHO",
        "trusted": true
      },
      "source": [
        "X4 = pd.concat([X2,X3],axis=1)"
      ],
      "execution_count": 177,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "spjHeeOQ1QDS",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "9bf9f9cc-29bf-46b9-cfc7-5129e76cb0ce"
      },
      "source": [
        "X4.shape"
      ],
      "execution_count": 178,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(14640, 10820)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 178
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YvsvIcZO1StF",
        "trusted": true
      },
      "source": [
        "x_train,x_test,y_train,y_test = train_test_split(X4,y,test_size=0.2,random_state=42)\n"
      ],
      "execution_count": 179,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7sb2pL7R2Bav",
        "trusted": true
      },
      "source": [
        "from sklearn.ensemble import GradientBoostingClassifier\n",
        "gbk = GradientBoostingClassifier(random_state=42, n_estimators=100,min_samples_split=100)\n",
        "gbk.fit(x_train, y_train)\n",
        "gbk_predict = gbk.predict(x_test)"
      ],
      "execution_count": 180,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "T3XcdM_l38gj",
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "07447970-9f28-40c6-967e-56e3b1cef7fe"
      },
      "source": [
        "from sklearn.metrics import accuracy_score\r\n",
        "print(\"Gradient Boosting Score :\",accuracy_score(y_test,gbk_predict ))"
      ],
      "execution_count": 182,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Gradient Boosting Score : 0.8247950819672131\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "j8BVvLQvOD0j"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}