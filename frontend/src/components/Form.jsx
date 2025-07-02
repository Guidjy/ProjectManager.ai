export function Form({ fields, onSubmit }) {
  return (
    <form onSubmit={ (event) => {event.preventDefault(); onSubmit();} }>
      <fieldset className="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
        <legend className="fieldset-legend">Login</legend>
        {fields.map((field, index) => (
          <FormField
            key={index}
            label={field.label}
            type={field.type}
            placeholder={field.placeholder}
          />
        ))}
        <button type="submit" className="btn btn-primary my-2">login</button>
      </fieldset>
    </form>
  );
}


export function FormField({label, type, placeholder}) {
  return (
    <>
      <label className="label">{label}</label>
      <input type={type} className="input mb-2" placeholder={placeholder} />
    </>
  );
}