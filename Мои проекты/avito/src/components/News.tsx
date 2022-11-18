import React, {useCallback, useEffect, useState} from 'react';
import {Col, Layout, Row} from 'antd';
import {Story} from "./types";
import {fetchStory} from "../utils/api";
import {Comments} from "./Comments";
import { RedoOutlined } from '@ant-design/icons';
import {Link} from "react-router-dom";
import {Times} from "./NewsItem";
const { Content } = Layout;


export function News({match}:any) {

    const [stories, setStorie] = useState<Story>()
    const loadStorie = async () => {
        let id = match.params.id
        const storiData = await fetchStory(id)
        setStorie(storiData)
    }

    useEffect( ()=> {loadStorie();},[])
    const [update,setUpdate] = useState<number>(0);

    const handleClick = useCallback(()=>{
        setUpdate(update+1);
    },[update])

    return (
        <>
            <Row>
            <Col lg={24} md={24} xs={24}>
                <Row>
                    <Col lg={13} md={13} xs={13}>
                    <Link to={{pathname:`/`}}>
                        <div className="ButtonClass1">Назад</div>
                    </Link>
                    </Col>
                    <Col lg={10} md={10} xs={10}>
                    </Col>
                </Row>
                <Content className="NewsPage">
                    <Row>
                        <Col lg={24} md={20} xs={20} style={{padding:'1.5rem'}}>
                                <a href={`${stories?.url}`} style={{fontSize:'1.7rem',fontWeight:'bold',color:'#000000'}}>{stories?.title}</a>
                            <a
                                href={`${stories?.url}`}
                                style={{fontSize:'1.5rem',paddingLeft:'1rem'}}
                            >
                                ({stories?.url})
                            </a>
                        </Col>
                    </Row>
                    <Row style={{paddingLeft:'1.5rem',paddingRight:'1.5rem', paddingBottom:'1.5rem'}}>
                        <Col lg={24} md={20} xs={20}>
                            <span style={{fontSize:'1.5rem', fontWeight:'bold'}}>by{" "+stories?.by}</span>
                            <span style={{fontSize:'1.5rem',paddingLeft:'1rem'}}>{Times(Number(stories?.time))}</span>
                            <span style={{fontSize:'1.5rem',paddingLeft:'1rem'}}>{ stories?.kids!==undefined ? Number(stories?.kids.length) + ' comments':'0'}</span>
                        </Col>
                    </Row>
                </Content>
                <Content>
                    <RedoOutlined onClick={handleClick} className="Icons" />
                <h2 className="CommentsPage">
                    {stories?.kids.map((it, index) => (
                            <Comments key={Number(it)} id={Number(it)}  update={update}/>
                    ))}
                </h2>
                </Content>
            </Col>
        </Row>
        </>
    )
}