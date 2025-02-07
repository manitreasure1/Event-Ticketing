

export default function RegisterOrg() {
  return (
    
    <div className="register_form form_container">
        <fieldset>
            <legend>Register Organization</legend>
            <form action="" method="post" encType="multipart/form-data">
                <div>
                    <label htmlFor="name">Name</label>
                    <input type="text" name="name"  placeholder="Organization name"/>
                </div>
                <div>
                    <label htmlFor="email">Email</label>
                    <input type="email" name="email" id="" placeholder="Organization email"/>
                </div>
                <div>
                    <label htmlFor="description">About the organization</label>
                    <textarea name="description" cols="30" rows="10" placeholder="Description ..."></textarea>
                </div>
                <div>
                    <button type="submit">Create</button>
                </div>
            </form>
        </fieldset>
    </div>
  )
}
