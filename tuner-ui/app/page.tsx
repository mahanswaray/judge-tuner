"use client";

import Image from "next/image";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import Example from "@/components/Example";
import { useState } from "react";
import Link from "next/link";

type Example = {
  id: number;
  input: string;
  output: string;
}

export default function Home() {
  // Make sure min examples are met
  // const [examples, setExamples] = useState<Example[]>([{ id: 1, input: "", output: "" }, { id: 2, input: "", output: "" }, { id: 3, input: "", output: "" }]);
  // TODO move to form let it handle state
  const [exampleCount, setExampleCount] = useState(0);
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.target as HTMLFormElement);
    console.log(formData.get("system-prompt"));
    formData.forEach((value, key) => {
      // TODO format appropriately or send to backend as form to handle
      console.log(key, value);
    });
  }
  const handleAddExample = () => {
    setExampleCount(exampleCount + 1);
  }
  const handleRemoveExample = () => {
    setExampleCount(exampleCount - 1);
  }
  // const handleChangeExampleInput = (id: number, input: string) => {
  //   setExamples(examples.map((example) => example.id === id ? { ...example, input } : example));
  // }
  // const handleChangeExampleOutput = (id: number, output: string) => {
  //   setExamples(examples.map((example) => example.id === id ? { ...example, output } : example));
  // }
  return (
    <main>
      <div className="px-5 pt-5">
      <h1 className="text-2xl font-bold tracking-tighter">
        Setup
      </h1>
      <p className="px-5 pt-5 text-sm">
        Something something instrutions. Please provide at least 3 examples.
      </p>
      </div>
      <form onSubmit={handleSubmit}>
      <div className="p-6">
        <h3 className="text-lg font-bold tracking-tighter">System Prompt</h3>
        <Textarea name="system-prompt" rows={10} placeholder="Type your message here." />
      </div>
      <div className="p-6 flex flex-col gap-6">
        {
          Array.from({ length: exampleCount }).map((_, index) => (
            <Example key={index} id={index + 1} />
          ))
        }
        <Button onClick={handleAddExample}>+</Button>
        <Button onClick={handleRemoveExample}>-</Button>
        <Button type="submit">submit</Button>
        <Link href="/main">
        <div className="border-2 border-red-500 w-24">
        temp link
        </div>
        </Link>
      </div>
      </form>
    </main>
  );
}
