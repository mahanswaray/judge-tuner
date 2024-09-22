"use client"

import ExampleForm from "@/components/ExampleForm"
import { Button } from "@/components/ui/button"

export default function AddPage() {
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.target as HTMLFormElement);
    console.log(formData.get("system-prompt"));
    formData.forEach((value, key) => {
      // TODO format appropriately or send to backend as form to handle
      console.log(key, value);
    });
  }
  return (
    <div>
      <h1 className="text-2xl font-bold">Add a new test</h1>
      <p className="text-sm text-gray-500">
        Add a new test to the system.
      </p>
      <form onSubmit={handleSubmit}>
        <ExampleForm />
        <Button type="submit">Add</Button>
      </form>
    </div>
  )
}