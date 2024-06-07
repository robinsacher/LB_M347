package main

import (
	"encoding/json"
	"log"
	"net/http"
)

type Joke struct {
	Joke string
}

func main() {

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		j := map[string]interface{}{
			"joke": "Why do blind programmers use Java? Because they can't C#.",
		}
		js, _ := json.Marshal(j)
		w.Header().Add("Content-Type", "application/json")
		w.Write(js)
	})

	log.Fatal(http.ListenAndServe(":3001", nil))

}
