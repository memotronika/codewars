// Thinkful - Logic Drills: Traffic light
func update_light(_ current_state: String) -> String {
    if current_state == "green" {
        return "yellow"
    } else if current_state == "yellow" {
        return "red"
    } else if current_state == "red" {
        return "green"
    } else {
        return "invalid state"
    }
}

// String repeat
func repeatStr(_ n: Int, _ string: String) -> String {
  var newline=""
  for i in 0..<n {
    newline += string
}

  return newline
}

// Function 1 - hello world
func greet() -> String {return "hello world!"}
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
