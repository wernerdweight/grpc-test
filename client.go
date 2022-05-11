package main

import (
	"bufio"
	"context"
	"google.golang.org/grpc"
	"log"
	"os"
	"time"
	"github.com/wernerdweight/grpc-test/ovm"
)

const (
	address = "localhost:50051"
)

func main() {
	// connect to server
	conn, _ := grpc.Dial(address, grpc.WithInsecure())
	defer conn.Close()
	client := ovm.NewOtazkyVaclavaMoravceClient(conn)

	// read arguments
	if len(os.Args) < 2 {
		log.Fatal("Not enough arguments!")
	}
	mood := os.Args[1]
	var sport ovm.Sport
	if len(os.Args) > 2 {
		inputSport := ovm.Sport(ovm.Sport_value[os.Args[2]])
		sport = inputSport
	}
	var booze ovm.Booze
	if len(os.Args) > 3 {
		inputBooze := ovm.Booze(ovm.Booze_value[os.Args[3]])
		booze = inputBooze
	}

	// call
	ctx, cancel := context.WithTimeout(context.Background(), time.Minute)
	defer cancel()
	var results *ovm.Response
	var reader = bufio.NewReader(os.Stdin)
	//for _, char := range bloke {
	for {
		char, _, _ := reader.ReadRune()
		switch char {
		case 'M':
			results, _ = client.VaclavMoravec(ctx, &ovm.MoravecRequest{
				Mood: ovm.Mood(ovm.Mood_value[mood]),
			})
		case 'K':
			results, _ = client.VaclavKlaus(ctx, &ovm.KlausRequest{
				Mood: ovm.Mood(ovm.Mood_value[mood]),
				Sport: sport,
			})
		case 'Z':
			results, _ = client.MilosZeman(ctx, &ovm.ZemanRequest{
				Mood: ovm.Mood(ovm.Mood_value[mood]),
				Booze: booze,
			})
		default: continue
		}
		log.Printf("%c (score %d): %v", char, results.Score, results.Sentences[0].Text)
	}
}
