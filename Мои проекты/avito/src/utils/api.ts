import { Story, Comment } from "../components/types"

export const HN_HOST = "https://hacker-news.firebaseio.com/v0"

export const fetchTopStoriesIds = async (): Promise<number[]> => {
    const response = await fetch(`${HN_HOST}/topstories.json`)
    const topStoriesIds = await response.json()
    return topStoriesIds
}

export const fetchStory = async (id: number): Promise<Story> => {
    const response = await fetch(`${HN_HOST}/item/${id}.json`)
    const storyData = await response.json()

    const story: Story = {
        id: storyData.id,
        by: storyData.by,
        score: storyData.score,
        title: storyData.title,
        time: storyData.time,
        url: storyData.url,
        kids:storyData.kids
    }
    return story
}
export const fetchComment = async (id: number): Promise<Comment> => {
    const response = await fetch(`${HN_HOST}/item/${id}.json`)
    const commentData = await response.json()

    const comment: Comment = {
        id: commentData.id,
        by: commentData.by,
        time: commentData.time,
        text: commentData.text,
        kids: commentData.kids
    }
    return comment
}

export const fetchStories = async (ids: number[]): Promise<Story[]> => {
    const stories = await Promise.all(ids.map(fetchStory))
    return stories
}