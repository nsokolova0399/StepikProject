import React from "react"
import { NavLink } from 'react-router-dom';
import { PageHeader } from 'antd';
import { Layout } from 'antd';
import { Col, Row } from 'antd';
const { Content } = Layout;

export function  MyHeader() {
    return(
        <Row>
            <Col lg={24} md={24} xs={24}>
            <PageHeader className="HeaderClass">
                    <NavLink to="/">
                        <Content className="ButtonClass">
                            Главная страница
                        </Content>
                    </NavLink>
                 </PageHeader>
            </Col>
        </Row>
    );
}
