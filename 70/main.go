package main

import "fmt"
import "bufio"
import "os"
import "strings"
import "strconv"

func main() {
    file, _ := os.Open(os.Args[1])
    defer file.Close()
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
      var line = scanner.Text()
      var strs = strings.Split(line, ",")
      var sq [8]int
      for i, v := range strs {
        sq[i], _ = strconv.Atoi(v)
      }
      var res = ""
      if (sq[0] > sq[4] || sq[2] > sq[6] || sq[1] < sq[5] || sq[3] < sq[7]) {
        res = "True"
      } else {
        res = "False"
      }
      fmt.Println(res)
    }
}
