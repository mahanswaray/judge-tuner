"use client"

import { useState } from "react";
import { Button } from "@/components/ui/button";
import Example from "./Example";


export default function ExampleForm() {
  const [exampleCount, setExampleCount] = useState(0);
  const handleAddExample = (e) => {
    e.preventDefault(); // Prevent form submission
    setExampleCount(exampleCount + 1);
  }
  const handleRemoveExample = (e) => {
    e.preventDefault(); // Prevent form submission
    setExampleCount(exampleCount - 1);
  }
  return (
    <div className="p-6 flex flex-col gap-6">
      {
        Array.from({ length: exampleCount }).map((_, index) => (
          <Example key={index} id={index + 1} />
        ))
      }
      <Button onClick={handleAddExample}>+</Button>
      <Button onClick={handleRemoveExample}>-</Button>
    </div>
  )
}