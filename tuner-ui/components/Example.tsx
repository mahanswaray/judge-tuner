import { Input } from "@/components/ui/input";

interface ExampleProps {
id: number
}

export default function Example({id}: ExampleProps) {
  return (
    <div className="flex flex-col">
        <h3 className="text-lg font-bold tracking-tighter py-2">Example {id}</h3>
        <p className="text-sm py-1">Input</p>
        <Input name={`example-${id}-input`} placeholder="TODO placeholder message" />
        <p className="text-sm py-1">Output</p>
        <Input name={`example-${id}-output`} placeholder="TODO placeholder message" />
    </div>
  )
}
