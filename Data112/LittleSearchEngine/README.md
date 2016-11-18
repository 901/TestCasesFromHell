#What Are These Files...?

Yes. These are seriously the testcases. Religious texts offer an interesting variety of words to search and they're nice and large. See the [end of this README](./README.md#the-texts) if you're interested in the particular texts.

`theHeavenlyTestCase.txt` lists all the other files (for use in `makeIndex`). The `noisewords.txt` is as of last year's assignment and is here for consistency.

#The Testcases

This assumes that you have a working driver. Since one is not provided with the assignment, one is not provided here. All that is noted is the first keyword, the second keyword, and the list of documents produced by the use of Linux tools emulating `top5search` (detailed below). That said, this maybe imperfect, so if you have a legitimate disagreement, please let us know. Enjoy (some of these are genuinely surprising)!

Keyword 1 | Keyword 2 | Result list | Notes
--- | --- | --- | ---
Israel | Holy | shemot.txt, avesta.txt, quran.txt, guruGranthSahib.txt, gita.txt | _genesis1.txt may appear instead of gita.txt_
God | Israel | quran.txt, shemot.txt, gita.txt, guruGranthSahib.txt, genesis1.txt | 
God | created | quran.txt, avesta.txt, shemot.txt, gita.txt, guruGranthSahib.txt | 
Persia | rain | quran.txt, genesis1.txt | _order may vary_
Persia | knife | null | _nothing worked here_
light | knife | guruGranthSahib.txt, quran.txt, gita.txt, genesis1.txt, avesta.txt | _quran.txt and gita.txt could be swapped as can genesis1.txt and avesta.txt_
love | war | gita.txt, guruGranthSahib.txt, quran.txt, genesis1.txt |
knife | noon | null |
moon | noon | gita.txt, avesta.txt | _order may differ - all should have a frequency of 1_
river | harvest | avesta.txt, shemot.txt, gita.txt, quran.txt, guruGranthSahib.txt
have | want | null | _Both are noise words._
ain't | don't | null | _Neither are keywords. Your driver should catch the fact or produce null_
have | haven't | null | _A noise word and a non-keyword._

#The Testing Tool Used

The tool used to produce the above table relies on Linux (or UNIX, POSIX, GNU) utilities. The tool goes through the files and prints out the number of occurances of the passed-in search term for each file.

Note that it does not care about noise words, punctuation, and all the malarkey that Sesh added.

#The Texts

So... what are the texts?

* avesta.txt: This is the Zoroastrian holy book. [Here's what that religion is.](https://en.wikipedia.org/wiki/Zoroastrianism) The excerpt is the beginning with the translator's comments included (they are interesting).
* genesis1.txt: This is from the Bible's book of Genesis. [Here's what that's about.](https://en.wikipedia.org/wiki/Christianity) This is the first three chapters, about the creation of the world.
* gita.txt: This is from the Bhagvad Gita (or Geeta). [It's Hindu.](https://en.wikipedia.org/wiki/Hinduism) This one is about a war, so there are some inflated word counts.
* guruGranthSahib: This is the Sikh holy book. [This is what Sikhism is.](https://en.wikipedia.org/wiki/Sikhism) This is also from the beginning.
* quran.txt: This is from the beginning of the Quran. [Here's where the Quran is from.](https://en.wikipedia.org/wiki/Islam) This is from the beginning, so Prophet Muhammad discusses his inspiration for a large portion.
* shemot.txt: This is the Torah's coverage of the Exodus. [This is where the Torah's from.](https://en.wikipedia.org/wiki/Judaism) [The Exodus](https://en.wikipedia.org/wiki/Book_of_Exodus) is a long story, this is its beginning.
