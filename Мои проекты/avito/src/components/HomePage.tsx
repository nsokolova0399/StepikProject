import React, {useCallback, useEffect, useState} from "react"
import { NewsItem } from "./NewsItem"
import { Story } from "./types"
import { fetchStories, fetchTopStoriesIds} from "../utils/api"
import { Layout } from 'antd';
import { RedoOutlined } from '@ant-design/icons';
const { Content } = Layout;


export function HomePage() {
    const [stories, setStories] = useState<Story[]>([])
    const loadStories = async () => {
        const topStoriesIdsData = await fetchTopStoriesIds()
        const storiesData = await fetchStories(topStoriesIdsData.slice(0, 99))
        setStories(storiesData)
    }

    const [state, setState]=useState<number>(0);

    const handleClick = useCallback(()=>{
        setState(state+1)
    }, [state])

    useEffect( ()=> {loadStories();},[state])

    setTimeout(() => {
        loadStories();
    }, 60000);
    return (
        <>
             <Layout>
            <Content style={{marginLeft:'auto', marginRight:'auto', marginTop:'1rem'}}>
                <RedoOutlined onClick={handleClick} className="Icons" />
                {stories.map((it, index) => (
                    <NewsItem key={it.id} id={it.id} title={it.title} score={it.score} by={it.by} time={it.time} url={it.url} index={index} />
            ))}
            </Content>
        </Layout>
</>
    )
}