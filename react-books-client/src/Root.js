import React from "react";
import withRoot from "./withRoot";
import {Query} from 'react-apollo';
import {gql} from "apollo-boost";

const Root = () => (
<Query query={GET_TRACKS_Q}>
{({ data, loading, error })=> {
    if (loading) return <div>loading...</div>
    if (error) return <div>error</div>

    return <div>{JSON.stringify(data)}</div>
}}

</Query>
);

const GET_TRACKS_Q = gql`
{
    books {
        id
        title
        author
        description
    }
}
`

export default withRoot(Root);
