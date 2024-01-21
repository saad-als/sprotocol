function MessageBox() {
    return (
        <>

            <div className="input-group mb-3 border  border-secondary rounded-2">
                <input type="text" className="form-control" placeholder="" aria-label="" aria-describedby="button-addon2" />
                <button className="btn btn-outline-success " type="button" id="button-addon2"><img src="../../../assets/send.svg" alt="" /></button>
            </div>

        </>
    );
}


export default MessageBox