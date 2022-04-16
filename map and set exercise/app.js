//What does the following code return?

new Set([1, 1, 2, 2, 3, 4]); //[1,2,3,4]

//Quick Question #2

const ref = [...new Set("referee")].join("");

//What does the Map m look like after running the following code?

let m = new Map();
m.set([1, 2, 3], true);
m.set([1, 2, 3], false);

// 0: {Array(3) => true}
//1: {Array(3) => false}

//Write a function called hasDuplicate which accepts an array and returns true or false if that array contains a duplicate

const hasDuplicate = (arr) => new Set(arr).size !== arr.length;

function containsVowel(vowel) {
  return "aeiou".includes(vowel);
}

function vowelCount(str) {
  const vowelMap = new Map();
  for (let char of str) {
    if (containsVowel(char)) {
      if (vowelMap.has(char)) {
        vowelMap.set(char, vowelMap.get(char) + 1);
      } else {
        vowelMap.set(char, 1);
      }
    }
  }
  return vowelMap;
}
