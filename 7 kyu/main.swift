// Find all non-consecutive numbers
func allNonConsecutive(_ arr: [Int]) -> [(Int, Int)] {
    guard arr.count > 1 else { return [] }
    var nonConsecutiveNumbers = [(Int, Int)]()
    for (index, number) in arr.enumerated() {
        if index == 0 {
            continue
        }
        let previousNumber = arr[index - 1]
        if number != previousNumber + 1 {
            nonConsecutiveNumbers.append((index, number))
        }
    }
    return nonConsecutiveNumbers
}

// Valid Parentheses
func validParentheses(_ str: String) -> Bool {
  var myArr = Array(str)
  if myArr.count % 2 != 0{return false}
  while myArr.count>0{
    if myArr[0] == ")" || myArr[myArr.count-1] == "("{return false}
    myArr.remove(at:0)
    for i in 0..<myArr.count{
      if myArr[i] == ")"{
        myArr.remove(at:i)
        break
      }
    }
  }
  return true
}

// Credit Card Mask
func maskify(_ str: String) -> String {
    let count = str.count
    guard count > 4 else { return str }
    
    let lastFour = String(str.suffix(4))
    let remaining = String(repeating: "#", count: count - 4)
    
    return remaining + lastFour
}

// 
// 
// 
// 
// 
// 
// 
// 
// 
