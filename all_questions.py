# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    level1["smoking"] = 1.0
    level1["smoking_info_gain"] = 0.278

    level1["cough"] = 0.0
    level1["cough_info_gain"] = 0.035

    level1["radon"] = 0.0
    level1["radon_info_gain"] = 0.236

    level1["weight_loss"] = 0.0
    level1["weight_loss_info_gain"] = 0.029

    level2_left["smoking"] = -1.0
    level2_left["smoking_info_gain"] = -1.0
    level2_right["smoking"] = -1.0
    level2_right["smoking_info_gain"] = -1.0

    level2_left["radon"] = 1.0
    level2_left["radon_info_gain"] = 0.722

    level2_left["cough"] = -1.0
    level2_left["cough_info_gain"] = -1.0

    level2_left["weight_loss"] = -1.0
    level2_left["weight_loss_info_gain"] = -1.0

    level2_right["radon"] = -1.0
    level2_right["radon_info_gain"] = -1.0

    level2_right["cough"] = 1.0
    level2_right["cough_info_gain"] = 0.722

    level2_right["weight_loss"] = -1.0
    level2_right["weight_loss_info_gain"] = -1.0

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up `construct_tree``
    # tree, training_error = construct_tree()
    tree = u.BinaryTree("root")  # MUST STILL CREATE THE TREE *****
    answer["tree"] = tree  # use the Tree structure
    # answer["training_error"] = training_error
    answer["training_error"] = 0.0  

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}

    # Answers are floats
    answer["(a) entropy_entire_data"] = 1.425
    # Infogain
    answer["(b) x < 0.2"] = 1.190
    answer["(b) x < 0.7"] = 1.118
    answer["(b) y < 0.6"] = 0.945

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = "y=0.6"  

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("y=0.6")
    tree.left = u.BinaryTree("x=0.2")
    tree.right = u.BinaryTree("x=0.7")
    tree.left.left = u.BinaryTree("y=0.8")
    tree.left.right = u.BinaryTree("Class A")
    tree.left.left.left = u.BinaryTree("Class B")
    tree.left.left.right = u.BinaryTree("Class C")
    tree.right.right = u.BinaryTree("y=0.3")
    tree.right.right.left = u.BinaryTree("Class C")
    tree.right.right.right = u.BinaryTree("Class A")
    tree.right.left = u.BinaryTree("Class B")

    answer["(d) full decision tree"] = tree

    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

    # float
    answer["(a) Gini, overall"] = 0.5

    # float
    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = 0.42
    answer["(d) Gini, Car type"] = 0.156
    answer["(e) Gini, Shirt type"] = 0.491

    answer["(f) attr for splitting"] = "Car type"

    # Explanatory text string
    answer["(f) explain choice"] = "Lowest GINI Index, i.e. lowest impurity compared to ID, Gender, and Shirt Type"

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    answer["a"] = ['binary', 'qualitative', 'nominal']

    # Explain if there is more than one interpretation. Repeat for the other questions. At least five words that form a sentence.
    answer["a: explain"] = "Only two categories with no order or measure"

    answer["b"] = ['continuous', 'quantitative', 'ratio']
    answer["b: explain"] = "Range of values for brightness, true zero point"

    answer["c"] = ['discrete', 'qualitative', 'ordinal']
    answer["c: explain"] = "Can be categorized by judgement, but unable to precisely measure with the naked eye"

    answer["d"] = ['continuous', 'quantitative', 'interval']
    answer["d: explain"] = "Range of values with no true zero (0 is still an angle measurement)"

    answer["e"] = ['discrete', 'qualitative', 'ordinal']
    answer["e: explain"] = "Implied ordered categories in terms of final standings, but no quantifiable difference represented in the medals themselves"

    answer["f"] = ['continuous', 'quantitative', 'ratio']
    answer["f: explain"] = "Can be measured precisely and with a true zero"

    answer["g"] = ['discrete', 'quantitative', 'ratio']
    answer["g: explain"] = "Countable quantity with a true zero"

    answer["h"] = ['discrete', 'qualitative', 'nominal']
    answer["h: explain"] = "Categorization of books with no quantitative value or order"

    answer["i"] = ['discrete', 'qualitative', 'ordinal']
    answer["i: explain"] = "Categories with natural order with no measureable quantities"

    answer["j"] = ['discrete', 'qualitative', 'ordinal']
    answer["j: explain"] = "Categories with natural order with no measureable quantities"

    answer["k"] = ['continuous', 'quantitative', 'ratio']
    answer["k: explain"] = "Can be measured precisely and has a true zero point"

    answer["l"] = ['continuous', 'quantitative', 'ratio']
    answer["l: explain"] = "Can be measured precisely and has a true zero point"

    answer["m"] = ['discrete', 'qualitative', 'nominal']
    answer["m: explain"] = "No measurable quantities or order"

    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = "Model 2"
    explain["a explain"] = "Because Model 2 is pruned, the complexity of the decision tree is reduced. This will lead to better performance with any new data set as it has reduced the number of redundant sections and the possibility of overfitting"

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = "Model 1"
    explain["b explain"] = "Higher classification accuracy as outlined by the equations (.85 > .81"

    explain["c similarity"] = "Both aim to prevent overfitting"
    explain["c similarity explain"] = "Both MDL and PEE consider model complexity and discourage overly complex models to prevent overfitting"

    explain["c difference"] = "How they work"
    explain["c difference explain"] = "MDL uses description length to quantify the relationship between model complexity and the fit of the data. PEE adjusts the error rate by adding increases with complexity and decreases with confidence in the error estimate"

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = "x<=0.5"
    answer["a, level 2, right"] = "A"
    answer["a, level 2, left"] = "y<=0.4"
    answer["a, level 3, left"] = "B"
    answer["a, level 3, right"] = "A"

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    answer["b, expected error"] = 0.06

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("x<=0.5")
    tree.left = u.BinaryTree("y<=0.4")
    tree.right = u.BinaryTree("A")
    tree.left.left = u.BinaryTree("B")
    tree.left.right = u.BinaryTree("A")
    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    answer["a, info gain, ID"] = 1.0
    answer["b, info gain, Handedness"] = 0.531

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "ID"

    # answer is a float
    answer["d, gain ratio, ID"] = 0.232
    answer["e, gain ratio, Handedness"] = 0.531

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Handedness"

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)

