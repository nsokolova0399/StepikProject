import React, {useEffect, useState, useCallback} from "react"
import {Comment} from "./types";
import {fetchComment} from "../utils/api";
import {Col, Row} from 'antd';
import { DownSquareTwoTone,UpSquareTwoTone } from '@ant-design/icons';

type CommentsProps = {
    id: number
    update:number
}

export function Comments({ id, update }: CommentsProps) {
    const [comments, setComments] = useState<Comment>()
    const loadComment = async () => {
        const storiComment = await fetchComment(id)
        setComments(storiComment)
    }

    useEffect( ()=> {
            loadComment();
    },[update])

    function createMarkup() { return {__html: `${comments?.text}`}; };

    const [state, setState]=useState<boolean>(false);

    const handleClick = useCallback(()=>{
        if(state){
        setState(false)
        }else{
            setState(true)
        }
    }, [state])

    return (
        <>
            <Row>
                <Col lg={24} md={24} xs={24}>
                    <div dangerouslySetInnerHTML={createMarkup()} />
                    <div>
                        {
                            state ?  <UpSquareTwoTone onClick={handleClick} style={{fontSize:'2rem'}}/>:<DownSquareTwoTone onClick={handleClick} style={{fontSize:'2rem'}}/>
                        }
                    </div>
                    <div>
                        {
                            comments?.kids!==undefined && state ?  comments?.kids.map((it, index) => (<div style={{marginLeft:'1.5rem', backgroundColor:'#29272712',padding:'0.4rem'}}><Comments key={it} id={Number(it)}  update={update} /></div>)):""
                        }
                    </div>
                </Col>
            </Row>
        </>
    )
}