export async function POST(req: Request, res: Response) {
  const body = await req.json();
  console.log(body);
  const response = await fetch("http://127.0.0.1:8000/set_up_task", {
    headers: {
      "Content-Type": "application/json"
    },
    method: "POST",
    body: JSON.stringify(body)
  })
  const data = await response.json();
  return new Response(JSON.stringify({ ...data }), { status: 200 });
}