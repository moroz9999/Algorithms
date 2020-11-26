import random


def gen_txt(len_):
    txt_ = ''
    for i in range(1 , len_):
        txt_ += str(chr(random.randint(97, 122)))
        #print(chr(random.randint(32, 127)), end='')
        # print(i, chr(i))
    # print(txt_)
    return txt_


def func(input_str):
    set_hashes = set()
    for i in range(len(input_str)):
        sub = input_str[i:]
        for j in range(1, len(sub) + 1):
            if not hash(sub[:j]) in set_hashes:
                set_hashes.add(hash(sub[:j]))
    print(len(set_hashes) - 1)
    # так и не смог избавиться "нормальным" путем от попадания всей исходной строки в множество,
    # костыльно вычитаю от результата единицу.


func("sova")
func("papa")
func(gen_txt(1000))
# func("It ought to be matter of surprise how men live in the midst of marvels, without taking heed of their existence. The slightest derangement of their accustomed walks in political or social life shall excite all their wonder, and furnish themes for their discussions, for months; while the prodigies that come from above are presented daily to their eyes, and are received without surprise, as things of course. In a certain sense, this may be well enough, inasmuch as all which comes directly from the hands of the Creator may be said so far to exceed the power of human comprehension, as to be beyond comment; but the truth would show us that the cause of this neglect is rather a propensity to dwell on such interests as those over which we have a fancied control, than on those which confessedly transcend our understanding. Thus is it ever with men. The wonders of creation meet them at every turn, without awakening reflection, while their minds labor on subjects that are not only ephemeral and illusory, but which never attain an elevation higher than that the most sordid interests can bestow.  For ourselves, we firmly believe that the finger of Providence is pointing the way to all races, and colors, and nations, along the path that is to lead the east and the west alike to the great goal of human wants. emons infest that path, and numerous and unhappy are the wanderings of millions who stray from its course; sometimes in reluctance to proceed; sometimes in an indiscreet haste to move faster than their fellows, and always in a forgetfulness of the great rules of conduct that have been handed down from above. Nevertheless, the main course is onward; and the day, in the sense of time, is not distant, when the whole earth is to be filled with the knowledge of the Lord, as the waters cover the sea.  One of the great stumbling-blocks with a large class of well- meaning, but narrow-judging moralists, are the seeming wrongs that are permitted by Providence, in its control of human events. Such persons take a one-sided view of things, and reduce all principles to the level of their own understandings. If we could comprehend the relations which the Deity bears to us, as well as we can comprehend the relations we bear to him, there might be a little seeming reason in these doubts; but when one of the parties in this mighty scheme of action is a profound mystery to the other, it is worse than idle, it is profane, to attempt to explain those things which our minds are not yet sufficiently cleared from the dross of earth to understand. Look at Italy, at this very moment. The darkness and depression from which that glorious peninsula is about to emerge are the fruits of long-continued dissensions and an iron despotism, which is at length broken by the impulses left behind him by a ruthless conqueror, who, under the appearance and the phrases of Liberty, contended only for himself. A more concentrated egotism than that of Napoleon probably never existed; yet has it left behind it seeds of personal rights that have sprung up by the wayside, and which are likely to take root with a force that will bid defiance to eradication. Thus is it ever, with the progress of society. Good appears to arise out of evil, and the inscrutable ways of Providence are vindicated by general results, rather than by instances of particular care. We leave the application of these remarks to the intelligence of such of our readers as may have patience to peruse the work that will be found in the succeeding pages.")
