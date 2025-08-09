fun main() {
    // Immutable variable (read-only)
    val appName: String = "My First Kotlin App"

    // Mutable variable
    var version = 1.0  // Type inferred as Double

    println("App: $appName, Version: $version")

    // Calling a function
    val sumResult = addNumbers(5, 10)
    println("Sum is: $sumResult")
}

// Function with parameters and return type
fun addNumbers(a: Int, b: Int): Int {
    return a + b
}

fun checkUserAge(age: Int) {
    if (age >= 18) {
        println("User is an adult")
    } else {
        println("User is a minor")
    }

    // Kotlin also supports 'when' (like switch in other languages)
    when (age) {
        in 0..12 -> println("Child")
        in 13..17 -> println("Teenager")
        else -> println("Adult")
    }
}

fun printNumbers() {
    // For loop
    for (i in 1..5) {
        println("Number: $i")
    }

    // While loop
    var count = 0
    while (count < 3) {
        println("Count: $count")
        count++
    }
}

class User(val name: String, var age: Int) {
    fun printInfo() {
        println("User: $name, Age: $age")
    }
}

fun main() {
    val user = User("Azamat", 25)
    user.printInfo()
    user.age = 26  // mutable property
    user.printInfo()
}

main()