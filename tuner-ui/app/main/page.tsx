"use client"

import { ScrollArea } from "@/components/ui/scroll-area"
import { useState } from "react"
import { Button } from "@/components/ui/button"
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
  } from "@/components/ui/dialog"
import {
    Table,
    TableBody,
    TableCaption,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
  } from "@/components/ui/table"
  import { Textarea } from "@/components/ui/textarea"

  import {
    HoverCard,
    HoverCardContent,
    HoverCardTrigger,
  } from "@/components/ui/hover-card"

  import { MessageSquarePlus } from "lucide-react"


function Feedback({question}: {question: string}) {
    const [feedback, setFeedback] = useState<string>("")
    const handleSubmit = () => {
        console.log(`Question: ${question} Feedback: ${feedback}`)
    }
    return (
<Dialog>
  <DialogTrigger>
    {/* TODO make it some icon */}

    <Button size="icon" variant="ghost" className="hover:bg-yellow-400"><MessageSquarePlus /></Button>
    </DialogTrigger>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>Submit Feedback for "{question}"</DialogTitle>
      <DialogDescription>
Description of what happens to update the eval.
      </DialogDescription>
      <Textarea rows={10} value={feedback} onChange={(e) => setFeedback(e.target.value)} />
      <Button className="w-20 h-8 bg-yellow-500 font-bold hover:bg-yellow-400" onClick={handleSubmit}>Submit</Button>
    </DialogHeader>
  </DialogContent>
</Dialog>
    )
}

const testEval = [
    {question: "Is the output a valid JSON?", score: "yes"},
    {question: "Percent JSON valid?", score: "0.8"},
    {question: "Category of something?", score: "blue"},
]

function EvalTable() {
    return (
<Table>
  <TableCaption>Is this caption needed?</TableCaption>
  <TableHeader className="bg-neutral-700">
    <TableRow>
      <TableHead>Question</TableHead>
      <TableHead>Score</TableHead>
      <TableHead>Feedback</TableHead>
    </TableRow>
  </TableHeader>
  <TableBody>
    {testEval.map((test) => (
        <TableRow>
            <TableCell className="font-medium">{test.question}</TableCell>
            <TableCell>
                <HoverCard openDelay={0}>
                    <HoverCardTrigger>
                        {test.score}
                    </HoverCardTrigger>
                    <HoverCardContent>
                        <p className="text-white">Reasoning for this score.</p>
                    </HoverCardContent>
                </HoverCard>
                </TableCell>
            <TableCell><Feedback question={test.question} /></TableCell>
        </TableRow>
    ))}
  </TableBody>
</Table>
    )
}



export default function Main() {
    const [currentTest, setCurrentTest] = useState<number | undefined>(undefined)
    const tests = []
    for (let i = 0; i < 100; i++) {
        tests.push({name: i+1, input: `input: ${i+1}`, output: `output: ${i+1}`, eval: `{"somefield": ${.01*(i+1)}}`})
    }
    return (
        <div className="grid grid-cols-4 h-[100vh]">
            <div className="col-span-1 overflow-y-auto border-r-2 border-gray-500">
                <ScrollArea>
                    {tests.map((test) => (
                        <Button onClick={() => setCurrentTest(test.name)} key={test.name} className="w-full rounded-none p-2 border-b border-gray-700 hover:bg-neutral-700">
                            {test.name}
                        </Button>
                    ))}
                </ScrollArea>
            </div>
            <div className="h-full col-span-3">
                {
                    currentTest ? (
                        <div className="p-4">
                        <h2 className="text-md font-bold">
                        Input
                        </h2>
                        <div className="p-2 m-2 border rounded-md border-gray-500 bg-neutral-700">
                            {tests.find((test) => test.name === currentTest)?.input}
                        </div>
                        <h2 className="text-md font-bold">
                            Output / Ground Truth
                            </h2>
                            <div className="p-2 m-2 border rounded-md border-gray-500 bg-neutral-700">
                            {tests.find((test) => test.name === currentTest)?.output}
                        </div>
                        <h2 className="text-md font-bold">
                            Model Output
                            </h2>
                            <div className="p-2 m-2 border rounded-md border-gray-500 bg-neutral-700">
                            {tests.find((test) => test.name === currentTest)?.output}
                        </div>
                            <h2 className="text-md font-bold">
                            Evaluation
                            </h2>
                            <EvalTable />
                        </div>
                    ) : (
                        <div>
                            Select a testcase to see results.
                        </div>
                    )
                }
            </div>
        </div>
    )
}


