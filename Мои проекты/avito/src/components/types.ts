export type Story = {
    id: number
    by: string
    score:string
    title: string
    time: number
    url: string
    kids:[]
}

export type Comment ={
    id: number
    by:string
    time: number
    text: string
    kids:[]
}