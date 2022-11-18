import React from "react"
import { CrownTwoTone, SmileTwoTone } from '@ant-design/icons';
import {Col, Layout, Row} from 'antd';
import { Link } from "react-router-dom";
const { Content } = Layout;

type NewsItemProps = {
    id: number
    title: string
    score: string
    by: string
    time: number
    url: string
    index: number
}

export function Times(time:number){
    let resTime = '';
    let res = Math.abs(Date.now() - time * 1000);
    let mins = Math.floor((res / (1000 * 60)) % 60);
    let hours = Math.floor((res / (1000 * 60 * 60)) % 24)
    let days = Math.floor(hours / 24);
    if(days !== 0) resTime = (days).toString() + ' days ago';
    else if (days === 0 && hours !== 0) resTime = (hours).toString() + ' hours ago';
    else if (days === 0 && hours === 0 && mins !== 0) resTime = (mins).toString() + ' minutes ago';
    else resTime = (mins).toString() + ' minutes ago';
    return resTime;
}
export function NewsItem({ id, title, score, by, time,url, index }: NewsItemProps) {
     return (
            <> <Row>
                <Col lg={24} md={24} xs={24}>
                    <Content className="ContentStyleExternal">
                        <Content className="ContentStyleInterior">
                            <Row>
                                <Col lg={22} md={22} xs={18}>
                                    <Link to={{pathname:`/News/${id}`}}>
                                        {index+1}. {title}
                                    </Link>
                                </Col>
                                <Col lg={1} md={1} xs={2}><CrownTwoTone /></Col>
                                <Col lg={1} md={1} xs={1}><div>{score}</div></Col>
                            </Row>
                            <Row>
                                <Col lg={1} md={1} xs={2}><SmileTwoTone /></Col>
                                <Col lg={18} md={18} xs={18}>by<span>{'  '+by}</span></Col>
                                <Col lg={5} md={5} xs={5}>{Times(time)}</Col>
                            </Row>
                        </Content>
                    </Content>
                </Col>
            </Row>
        </>
    )
}
