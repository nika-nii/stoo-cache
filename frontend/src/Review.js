import React, { useState, useEffect } from 'react';
import axios from 'axios'
import Select from "react-dropdown-select";
import Rating from '@material-ui/lab/Rating'
const TargetChooser = () => {

    const [options, setOptions] = useState()

    const [currentTarget, setCurrentTarget] = useState()

    const [reviewText, setReviewText] = useState("")

    const [rating, setRating] = useState(5)

    const fetchData = async () => {
        return await axios.get("http://localhost:8000/api/review_target/")
    }

    useEffect(() => {
        fetchData().then(res => setOptions(res.data))
    }, [])


    const sendReview = () => {
        const payload = { text: reviewText, rating: rating, target: currentTarget.id }
        axios.post("http://localhost:8000/api/review/", payload)
    }

    if (options) {
        return (
            <div className="container p-5">
                <div className="container px-5 py-3">
                    <Select
                        labelField={"name"}
                        required
                        searchable
                        searchBy={"name"}
                        values={[]}
                        options={options}
                        onChange={(value) => setCurrentTarget(value[0])}
                    />
                </div>
                <div className="container px-5 py-3">
                    <textarea class="form-control"
                        id="FormControlTextarea"
                        rows="3"
                        placeholder="Пишите, что вам понравилось, а что нет..."
                        value={reviewText}
                        onChange={(event) => { setReviewText(event.target.value) }}
                    >
                    </textarea>
                </div>
                <div className="d-flex justify-content-between px-5 py-3">

                    <Rating
                        name="hover-feedback"
                        defaultValue={5}
                        onChange={(event, newValue) => {
                            setRating(newValue)
                        }}
                    />
                    <button type="button" class="btn btn-dark" onClick={sendReview}>Отправить</button>
                </div>
            </div>
        )
    } else {
        return <div></div>
    }

}

export default TargetChooser