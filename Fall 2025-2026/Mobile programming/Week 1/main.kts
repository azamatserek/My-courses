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

main()