# def find_first_duplicate(arr)
#   if arr.length < 2
#     return nil
#   end

#   for i in 0..arr.length
#     for j in (i + 1)..arr.length - 1
#       if arr[i] == arr[j]
#         return arr[i]

#       end
#     end
#   end
#   return nil
# end
# p find_first_duplicate([0])

# Find the largest product of any two numbers within a given array.

# Input: [5, -2, 1, -9, -7, 2, 6]
# Output: 63 (-9 * -7)

#Input: [1, 5, 3, 8]
#Output: 40

#Input: []
#Output: nil

# def return_product(array)
#   product = 0

#   for i in 0..array.length
#     for j in (i + 1)..array.length - 1
#       if (array[i] * array[j]) > product
#        product = array[i] * array[j]
#       end
#     end
#   end
#  return product
# end

# p return_product([1, 5, 3, 8])

# i = 0
# j = i + 1

# while i <= array.length
#   while j < array.length - 1

#   end
# end

# Given two arrays of strings, return a new string that contains every combination of a string from the first array concatenated with a string from the second array.

# input = ["a", "b", "c"],
# ["d", "e", "f", "g"]

# Output: ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"]
# p input[1][0]

# arr = ""

# for i in 0..input.length
#  for j in 0..input[1].length - 1
#   arr << "#{input[0][i]}#{input[1][j]}"
#  end
# end
# p arr

# Given ONE array of strings, return a new array that contains every combination of each string with every other string in the array.

# Input: ["a", "b", "c", "d"]
# Output: ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"]

# def array_mesh_two(input)
#   new_arr = []
#   for i in 0...input.length
#     p input[i]
#     for j in 0...input.length
#       unless i == j
#         new_arr << "#{input[i]}#{input[j]}"
#       end
#     end
#   end
#   return new_arr
# end

# array_mesh_two(["a", "b", "c", "d"])


# The following hash table represents a particular person: { firstName: "Ada", lastName: "Lovelace", email: "ada.lovelace@email.com" }
# Write a function that accepts this type of hash table and returns the person's email address.



# The following hash table represents the inventory of shirts for a clothing store: { red: 500, blue: 615, green: 484, yellow: 332 }
# Write a function that accepts a hash table like this and adds 200 shirts to the "yellow" category. The function can then return the updated hash table.


def hash_function(hash, _new_color, _num_shirts)
  sum = hash.select(:+) { |hash| hash.values}
  sum
end
my_hash = { red: 500, blue: 615, green: 484, yellow: 332 }
color = :turquoise
num = 543
p hash_function(my_hash, color, num)