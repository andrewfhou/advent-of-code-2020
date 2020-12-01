main :: IO()
main = do
    inp <- readFile "input.txt"
    let vals = [read x :: Int | x <- lines inp]
    print $ [a * b | a <- vals, b <- vals, a + b == 2020]
    print $ [a * b * c | a <- vals, b <- vals, c <- vals, a + b + c == 2020]
