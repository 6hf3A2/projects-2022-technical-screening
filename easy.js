var assert = require("assert")
// Given an array of numbers, return a new array so that positive and negative
// numbers alternate. You can assume that 0 is a positive number. Within the
// positive and negative numbers, you must keep their relative order. You are 
// guaranteed the number of positive and negative numbers will not differ by more 
// than 1.

// =====Example 1
// Input: [1, -3, -8, -5, 10]
// Output: [-3, 1, -8, 10, -5]
// Explanation: We have alternated positive and negative numbers. Notice that the
// negative numbers appear in the same relative order (-3, -8, -5) and the positive
// numbers appear in the same order as well (1, 10).

// =====Example 2
// Input: [3, 0, 0, -5, -2]
// Output: [3, -5, 0, -2, 0]
// Explanation: We have alternated positive and negative numbers. Notice they appear
// in the same relative order.

// =====Example 3
// Input: [0, -3, 3, -1, 1, -1]
// Output #1: [0, -3, 3, -1, 1, -1]
// Output #2: [-3, 0, -1, 3, -1, 1]
// Explanation: There are 2 possible answers which satisfy the problem's constraints.
// We can start with either positive or negative

// =====Example 4
// Input numArray: []
// Output numArray: []
// Explanation: Empty array...

const altNumbers = (numArray) => {

    // case1: empty array given
    if (numArray == []) {
        return [];
    }

    // count the number of positive int and negative int
    var count_positive = 0;
    var count_negative = 0;
    for (var i = 0; i < numArray.length; i++) {
        if (numArray[i] < 0) {
            count_negative = count_negative + 1
        } else {
            count_positive = count_positive + 1
        }
    }

    // create an array of size of given array
    // set the element all to 0
    var total = count_positive + count_negative;
    var return_array = Array(total).fill(0);

    // index of positive and negative number in new array
    var count1 = 0;
    var count2 = 1;

    // case2: array start with positive number or start with negative number
    if (count_positive > count_negative) {
        for (var i = 0; i < return_array.length; i++) {
            if (numArray[i] >= 0) {
                return_array[count1] = numArray[i]
                // increase the index by 2
                count1 += 2
            } else {
                return_array[count2] = numArray[i]
                // increase the index by 2
                count2 += 2
            }
        }
    } else {
        for (var i = 0; i < return_array.length; i++) {
            if (numArray[i] >= 0) {
                return_array[count2] = numArray[i]
                // increase the index by 2
                count2 += 2
            } else {
                return_array[count1] = numArray[i]
                // increase the index by 2
                count1 += 2
            }
        }
    }
    return return_array
}


module.exports = { altNumbers } // Do not modify this line

// ====================TESTS====================
// Some tests to help you check your progress. Simply run your code with
// node easy.js
// If successful, no output should appear. If unsuccessful, you should see 
// assertion errors being thrown.

let array1 = [1, -3, -8, -5, 10]
array1 = altNumbers(array1)
const answer1 = [-3, 1, -8, 10, -5]
for (let i = 0; i < array1.length; i++) {
    assert(array1[i] === answer1[i])
}

let array2 = [3, 0, 0, -5, -2]
array2 = altNumbers(array2)
const answer2 = [3, -5, 0, -2, 0]
for (let i = 0; i < array2.length; i++) {
    assert(array2[i] === answer2[i])
}

let array3 = [0, -3, 3, -1, 1, -1]
array3 = altNumbers(array3)
const answer3a = [0, -3, 3, -1, 1, -1]
const answer3b = [-3, 0, -1, 3, -1, 1]
if (array3[0] === 0) {
    for (let i = 0; i < array3.length; i++) {
        assert(array3[i] === answer3a[i])
    }
} else if (array3[0] == -3) {
    for (let i = 0; i < array3.length; i++) {
        assert(array3[i] === answer3b[i])
    }
} else {
    assert(false)
}

let array4 = []
array4 = altNumbers(array4)
assert(array4.length === 0)

let array5 = [3,2,1,-1,-2,-3,-4]
array5 = altNumbers(array5)
const answer5 = [-1, 3, -2, 2, -3, 1, -4]
for (let i = 0; i < array5.length; i++) {
    assert(array5[i] === answer5[i])
}

let array6 = [5,-1,-2,-3,-4,0,3]
array6 = altNumbers(array6)
const answer6 = [-1, 5, -2, 0, -3, 3, -4]
for (let i = 0; i < array6.length; i++) {
    assert(array6[i] === answer6[i])
}
